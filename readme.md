# One billion matches

One billion matches is challenge to implement generic delivery algorithm, that may be suitable for variety of tasks.

To give you some context, you may think this problem as:
- delivering marketing email
- sending group messages in messaging platform
- delivering ads in the Internet

Read the problem definition below and implement your solution in solutions folder.


## Problem

There are 100 000 items that are classified to have N labels, here N is between 1 and 50.

There are 100 000 subscribers that are interested in items of specific labels, here again one subscriber may have 1 to 50 labels.

There are 50 000 labels.

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

```
[Item] --(has many)--> [Label] <--(has many)-- [Subscriber]
```



## Running example

To generate test data run:
`make generate`
This generates random test data in `data/data`

Build and run example solution:

`make build solution='example'`
`make run solution='example'`

This starts Docker container that runs until solution is found.

## Creating your solution

Give name to your solution, it should be filepath compatible, below we use `your-solution`

You can make copy of example solution:
`cp -r ./solutions/example ./solutions/your-solution`

Then you can implement your solution.

We expect to have various different solutions, so implement yours in Dockerfile.

There should be Dockerfile at `solutions/your-solution/Dockerfile`

Running the dockerfile should produce output file `solutions/your-solution/output/output.csv`

Document your solution and results in `solutions/your-solution/readme.md`


## Files

Input data contains three files as UTF-8 CSV:
- items.csv
- labels.csv
- subscribers.csv

Notes:
- First line is header containing column names
- Label ids in items and subscribers are joined in single column and can be separated by pipe character `|`
- Output file containing delivery solution should be UTF-8 CSV

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