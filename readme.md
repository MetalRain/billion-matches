# One billion matches

One billion matches is challenge to implement generic delivery algorithm, that may be suitable for variety of tasks.

To give you some context, you may think this problem as:
- delivering marketing email,
- sending group messages in messaging platform
- delivering ads in the Internet
- distributed filesystem write-ahead-log replication

Read the problem definition below and implement your solution in solutions folder.


## Problem

There are million items that are classified to have N labels, here N is between 1 and 100.

There are million subscribers that are interested in items of specific labels, here again one subscriber may have 1 to 100 labels.

There are up to 50 000 labels.

We are seeking for solution to efficiently calculate which items should each subscriber recieve.

Items have timestamps, subscribers want items ordered by timestamp.


### Models

Item:
- id
- timestamp
- label_ids

Label:
- id

Subscriber:
- id
- label_ids


### Relations

(Item) --[has]--> (Label) <--[interested in]-- (Subscriber)



## Running example

To generate test data, build & run example run:
`make run solution='example'`

This starts Docker container that runs until solution is found.

## Creating your solution

You can make copy of example solution:
`cp -r solutions/example solutions/your-solution`

Then you can implement your solution.

We expect to have various different solutions, so implement yours in Dockerfile.

It should produce output file `solutions/your-solution/output.csv` 


## Files

Input data contains three files as UTF-8 CSV:
- items.csv
- labels.csv
- subscribers.csv

Label ids are joined in single column and can be separated by pipe `|`

Output file containing delivery solution should be UTF-8 CSV

### Items.csv

```csv
id,timestamp,label_ids
1,2,2|4|6
2,1,5
3,3,6
```

### Labels.csv

```csv
id
2
4
5
6
```

### Subscribers.csv

```csv
id,label_ids
1,5|6
2,2
3,2|6
```

### Output.csv

Notes:
- item_ids should be ordered by timestamp 
- subscribers should be ordered by id
- same item cannot be sent twice to one subcriber even when matches multiple labels

```csv
subscriber_id,item_ids
1,2|1|3
2,1
3,1|3
```