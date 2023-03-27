.print 'Loading data'
.mode csv
.import /app/data/items.csv items
.import /app/data/subscribers.csv subscribers


.print 'Processing items'
CREATE TABLE items_with_labels(id integer, timestamp integer, label_id integer);
WITH split_items(id, timestamp, label_id, joined_ids) AS (
  SELECT 
    id,
    timestamp,
    '',
    label_ids || '|'
  FROM (SELECT * FROM items)
  UNION ALL SELECT
    id,
    timestamp,
    substr(joined_ids, 0, instr(joined_ids, '|')), -- each word contains text up to next '|'
    substr(joined_ids, instr(joined_ids, '|') + 1) -- next recursion parses ids after this '|'
  FROM split_items -- recurse
  WHERE joined_ids != '' -- break recursion no more labels to break
)
INSERT INTO items_with_labels SELECT
  cast(si.id as integer) as id,
  cast(si.timestamp as integer) as timestamp,
  cast(si.label_id as integer) as label_id
FROM split_items si
WHERE si.label_id != ''
ORDER BY timestamp;


.print 'Processing subscribers'
CREATE TABLE subscribers_with_labels(id integer, label_id integer);
WITH split_subscribers(id, label_id, joined_ids) AS (
  SELECT 
    id,
    '',
    label_ids || '|'
  FROM (SELECT * FROM subscribers)
  UNION ALL SELECT
    id,
    substr(joined_ids, 0, instr(joined_ids, '|')), -- each word contains text up to next '|'
    substr(joined_ids, instr(joined_ids, '|') + 1) -- next recursion parses ids after this '|'
  FROM split_subscribers -- recurse
  WHERE joined_ids != '' -- break recursion no more labels to break
)
INSERT INTO subscribers_with_labels SELECT 
  cast(ss.id as integer) as id,
  cast(ss.label_id as integer) as label_id
FROM split_subscribers ss
WHERE ss.label_id != ''
ORDER BY id;


.print 'Producing result file'
.headers on
.output /app/output/output.csv
SELECT
  s.id as subscriber_id,
  GROUP_CONCAT(i.id, '|') as item_ids
FROM subscribers_with_labels s
LEFT JOIN items_with_labels i
  ON (i.label_id = s.label_id)
GROUP BY s.id
ORDER BY s.id, i.timestamp;
.quit