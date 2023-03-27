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
0.00 user 0.06 system
2:16.66 elapsed 0% CPU
(0 avgtext+0 avgdata 53704 maxresident)k
0 inputs + 0 outputs (0 major + 4058 minor) pagefaults 0 swaps
```