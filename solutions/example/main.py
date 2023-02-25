import argparse
import csv
import gc
from typing import Dict, Tuple

from tqdm import tqdm

def main() -> None:
    parser = argparse.ArgumentParser(description='Billion matches example')
    parser.add_argument('labels')
    parser.add_argument('items')
    parser.add_argument('subscribers')
    args = parser.parse_args()

    # group items by label
    label_item_map: Dict[int, Dict[int, int]] = {}

    # read labels
    with open(args.labels) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in tqdm(r, desc='Read labels'):
            label_item_map[int(row[0])] = {}

    gc.collect()
        
    # read items
    with open(args.items) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in tqdm(r, desc='Read items'):
            id = int(row[0])
            ts = int(row[1])
            for l in split_ids(row[2]):
                # here we have assumption: one timestamp has only one item
                label_item_map[l][ts] = id

    gc.collect()

    subscribers: list[Tuple[int, list[int]]]  = []

    # read subscribers
    with open(args.subscribers) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in tqdm(r, desc='Read subscribers'):
            subscribers.append((
                int(row[0]),
                split_ids(row[1])
            ))

    gc.collect()

    # sort subscribers
    subscribers.sort(key=lambda sub: sub[0])

    # write result
    with open('./output/output.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['subscriber_id', 'item_ids'])

        for s_id, s_labels in tqdm(subscribers, desc='Process deliveries'):
            # collect matching items
            # dict deduplicates items
            items_to_deliver: Dict[int, int] = {}
            for l in s_labels:
                items_to_deliver.update(label_item_map[l])

            row = [
                str(s_id),
                # sort items by timestamp
                join_ids([i_id for i_ts, i_id in sorted(items_to_deliver.items())])
            ]
            w.writerow(row)

def split_ids(id_str) -> list[int]:
    return [int(id) for id in id_str.split('|')]

def join_ids(ids: list[int]) -> str:
    return '|'.join([str(id) for id in ids])

if __name__ == "__main__":
    main()
