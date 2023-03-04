import csv
import random
from typing import Tuple

from tqdm import tqdm

LABELS = 50_000
ITEMS = 100_000
LABELS_PER_ITEM = 50
SUBSCRIBERS = 100_000
LABELS_PER_SUBSCRIBER = 50

def main() -> None:
    # static seed to generate always same data
    random.seed(42)

    # generate data
    labels: list[int] = gen_range(LABELS)

    # output labels
    with open('./data/labels.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['id'])
        for label_id in tqdm(labels, desc='Write labels'):
            w.writerow([str(label_id)])

    item_ids = gen_range(ITEMS)
    random.shuffle(item_ids)
    item_timestamps = gen_range(ITEMS)
    random.shuffle(item_timestamps)
    items: list[Tuple[int, int, list[int]]] = [
        (id, ts, random.sample(labels, random.randint(1, LABELS_PER_ITEM+1)))
        for id, ts in tqdm(zip(item_ids, item_timestamps), desc='Gen items')
    ]

    # output items
    with open('./data/items.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['id', 'timestamp', 'label_ids'])
        for item in tqdm(items, desc='Write items'):
            w.writerow([str(item[0]), str(item[1]), join_labels(item[2])])
    items = []

    subscriber_ids = gen_range(SUBSCRIBERS)
    random.shuffle(subscriber_ids)
    subscribers: list[Tuple[int, list[int]]] = [
        (id, random.sample(labels, random.randint(1, LABELS_PER_SUBSCRIBER+1)))
        for id in tqdm(subscriber_ids, desc='Gen subscribers')
    ]

    # output subscribers
    with open('./data/subscribers.csv', 'w') as f:
        w = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONE)
        w.writerow(['id', 'label_ids'])
        for sub in tqdm(subscribers, desc='Write subscribers'):
            w.writerow([str(sub[0]), join_labels(sub[1])])
    subscribers = []

def join_labels(label_ids: list[int]) -> str:
    return '|'.join([str(label_id) for label_id in label_ids])

def gen_range(n: int) -> list[int]:
    return [int(id) for id in range(1, n+1)]

if __name__ == "__main__":
    main()
