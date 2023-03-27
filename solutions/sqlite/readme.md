# SQLite

This problem is actually just join and sort in relations.

So maybe SQLite would do well here.

This solution uses csv support in SQLite to parse and produce the result.


## Design

Load all files as tables

Join subscribers with subquery that finds timestamp ordered unique items by labels.


## Performance

```
Running solution: sqlite
Loading data
Processing items
Processing subscribers
Calculating result
Producing result file
0.02user 0.04system 1:36.04elapsed 0%CPU (0avgtext+0avgdata 52212maxresident)k
0inputs+0outputs (0major+3911minor)pagefaults 0swaps
```