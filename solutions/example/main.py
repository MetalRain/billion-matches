import argparse
import csv
from typing import Tuple

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

    # sort items
    items.sort(key=lambda item: item[1])

    # collect deliveries
    deliveries: list[Tuple[int, list[int]]] = []

    for s in subscribers:
        items_to_deliver: list[int] = []
        for i in items:
            for l in i[2]:
                if l in s[1]:
                    items_to_deliver.append(i[0])
                    break
        deliveries.append((s[0], items_to_deliver))

    # write result
    with open('./output/output.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['subscriber_id', 'item_ids'])
        for d in deliveries:
            w.writerow([
                str(d[0]),
                join_ids(d[1])
            ])

def split_ids(id_str) -> list[int]:
    return [int(id) for id in id_str.split('|')]

def join_ids(ids: list[int]) -> str:
    return '|'.join([str(id) for id in ids])

if __name__ == "__main__":
    main()
