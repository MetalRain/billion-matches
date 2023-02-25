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

    # read data
    labels: list[int] = []
    items: list[Tuple[int, int, list[int]]] = []
    subscribers: list[Tuple[int, list[int]]]  = []

    # read labels
    with open(args.labels) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in r:
            labels.append(int(row[0]))
        
    # read items
    with open(args.items) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in r:
            items.append((
                int(row[0]),
                int(row[1]),
                split_ids(row[2])
            ))

    # group items by label
    label_item_map: Dict[int, list[Tuple[int, int]]] = {l: [] for l in labels}
    for i in tqdm(items, desc='Items'):
        for l in i[2]:
            label_item_map[l].append((i[0], i[1]))

    # Free up memory
    items = []
    labels = []
    gc.collect()

    # read subscribers
    with open(args.subscribers) as f:
        r = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
        # skip header line
        r.__next__()
        for row in r:
            subscribers.append((
                int(row[0]),
                split_ids(row[1])
            ))

    # sort subscribers
    subscribers.sort(key=lambda sub: sub[0])

    # write result
    with open('./output/output.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['subscriber_id', 'item_ids'])

        for s_id, s_labels in tqdm(subscribers, desc='Subscribers'):
            # collect matching items
            items_to_deliver: Dict[int, int] = {
                i_ts: i_id
                for l in s_labels
                for i_id, i_ts in label_item_map[l]
            }

            # sort by timestamp
            row = [
                str(s_id),
                join_ids([i_id for i_ts, i_id in sorted(items_to_deliver.items())])
            ]
            w.writerow(row)

def split_ids(id_str) -> list[int]:
    return [int(id) for id in id_str.split('|')]

def join_ids(ids: list[int]) -> str:
    return '|'.join([str(id) for id in ids])

if __name__ == "__main__":
    main()
