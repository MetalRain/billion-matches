# Example solution

Example solution is implemented with Python, nothing too fancy.

Solution reads labels into memory, creating map from label -> items.
Then reads items into that map, here we also make assumption that one timestamp has only one item.
So within one label there is map from timestamp -> item id.

Then we read subcribers into memory, sort them by id.
Then we write subscribers into the result file one by one.
Subscribers items can be found via subscriber labels, we get back multiple maps
that we merge together. This produces map where one subscriber items are mapped by timestamp -> item id.
We sort that map by key (timestamp) and get values (item ids).

## Results

On Intel Core i7 9700K running in WSL I get following results:
```
Running solution: example
Read labels: 50000it [00:00, 1282622.55it/s]
Read items: 100000it [00:01, 79409.45it/s]
Read subscribers: 100000it [00:00, 158012.19it/s]
Process deliveries: 100%|██████████| 100000/100000 [01:06<00:00, 1494.44it/s]
0.10 user 0.14 system 1:11.57 elapsed 0% CPU
(0 avgtext+0 avgdata 52128 maxresident) k
1056 inputs + 0 outputs (8 major + 3898 minor) pagefaults 0 swaps
```
So 1 minute 12 seconds wall clock time.
