CREATE KEYSPACE shopping_elf WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;

CREATE TABLE shopping_elf.receipt_data (
    userid text,
    product_name text,
    bill_date date,
    qty double,
    time date,
    PRIMARY KEY (userid, product_name, bill_date)
) WITH CLUSTERING ORDER BY (product_name ASC, bill_date ASC)
