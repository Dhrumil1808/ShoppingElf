CREATE KEYSPACE shopping_elf WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;

CREATE TABLE shopping_elf.receipt_data (
    userid text,
    product_name text,
    bill_date date,
    qty double,
    time date,
    family_members int,
    PRIMARY KEY (userid, product_name, bill_date)
) WITH CLUSTERING ORDER BY (product_name ASC, bill_date ASC)

CREATE TABLE shopping_elf.products (
    product_name text,
    PRIMARY KEY (product_name)
)


CREATE TABLE shopping_elf.user (
    userid text,
    family_members int,
    username text,
    PRIMARY KEY (username)
)


insert into shopping_elf.user ("userid","family_members","username") values ('1',2,'rash');
