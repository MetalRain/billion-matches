# SQLite

This problem is actually just join and sort in relations.

So maybe SQLite would do well here.

This solution uses csv support in SQLite to parse and produce the result.


## Design

Load all files as tables

Join subscribers with subquery that finds timestamp ordered unique items by labels.


## Performance

On Intel Core i7 9700K running in WSL I get following results:
```
Running solution: sqlite
Loading data
Processing items
Processing subscribers
Calculating result
Producing result file
0.00user 0.07system 4:01.90elapsed 0%CPU (0avgtext+0avgdata 53120maxresident)k
0inputs+0outputs (0major+4139minor)pagefaults 0swaps
```
So 4 minutes and 2 seconds wall clock time.