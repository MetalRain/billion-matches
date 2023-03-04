load 'tables/csv'
items =: }. readcsv jpath '/app/data/items.csv'
subscribers =: }. readcsv jpath '/app/data/subscribers.csv'
subscriber_ids =: 1{. |: subscribers
echo subscriber_ids
subscriber_label_ids =: 1{ > 0{ subscribers
echo subscriber_label_ids
exit ''