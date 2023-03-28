import argparse
import csv
import gc
from typing import Dict, Tuple

from tqdm import tqdm

TimeIdMap = Dict[int, int]
LabelMap = Dict[int, TimeIdMap]
Subscriber = Tuple[int, list[int]]

def main() -> None:
    parser = argparse.ArgumentParser(description='Billion matches example')
    parser.add_argument('items')
    parser.add_argument('subscribers')
    args = parser.parse_args()

    label_item_map: LabelMap = read_items(args.items)
    gc.collect()

    subscribers: list[Tuple[int, list[int]]]  = read_subscribers(args.subscribers)
    gc.collect()

    write_result(subscribers, label_item_map)

def read_items(filepath: str) -> LabelMap:
    # group items by label
    label_item_map: LabelMap = {}
        
    # read items
    with open(filepath) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in tqdm(r, desc='Read items'):
            id = int(row[0])
            ts = int(row[1])
            for l in split_ids(row[2]):
                if l not in label_item_map:
                    label_item_map[l] = {}
                # here we have assumption: one timestamp has only one item
                label_item_map[l][ts] = id

    return label_item_map

def read_subscribers(filepath: str) -> list[Subscriber]:
    subscribers: list[Subscriber]  = []

    # read subscribers
    with open(filepath) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in tqdm(r, desc='Read subscribers'):
            subscribers.append((
                int(row[0]),
                split_ids(row[1])
            ))

    # sort subscribers
    subscribers.sort(key=lambda sub: sub[0])
    return subscribers

def write_result(subscribers, label_item_map) -> None:
    with open('./output/output.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['subscriber_id', 'item_ids'])

        for s_id, s_labels in tqdm(subscribers, desc='Process deliveries'):
            # collect matching items

            # dict deduplicates items
            items_to_deliver: TimeIdMap = {}
            for l in s_labels:
                items_to_deliver.update(label_item_map[l])

            row = [
                str(s_id),
                # sort items by timestamp
                join_ids([i_id for i_ts, i_id in sorted(items_to_deliver.items())])
            ]
            w.writerow(row)

def split_ids(id_str: str) -> list[int]:
    return [int(id) for id in id_str.split('|')]

def join_ids(ids: list[int]) -> str:
    return '|'.join([str(id) for id in ids])

if __name__ == "__main__":
    main()
