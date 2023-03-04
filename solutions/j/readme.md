# J

This solution uses [J programming language](https://www.jsoftware.com) APL like array programming language, that may allow problem solved with elegance.

## Libraries used
CSV addon: https://code.jsoftware.com/wiki/Addons/tables/csv


## Program

Read items into vectors:
- [id, [labels]]
- [id, timestamp]

Read subscribers into vector:
- [id, [labels]]

For each subscriber:

    Create matching [table](https://www.jsoftware.com/help/dictionary/d420.htm)

    `matches =: subscriber_labels =/ items_labels`

    0 1 0 1 0 ...
    0 0 0 0 0 ...
    0 0 0 1 0 ...
    ...

    Multiply table with item ids

    0 (1 * Id2) 0 (1 * Id4) 0
    0 0         0 0         0
    0 0         0 (1 * Id4) 0

    Filter zeros and reshape into vector

    Id2 Id4 Id4

    [Deduplicate](https://www.jsoftware.com/help/dictionary/d221.htm)

    Id2 Id4

    Sort by item timestamps

    Id4 Id2