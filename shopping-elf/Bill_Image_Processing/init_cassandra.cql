CREATE KEYSPACE shopping_elf WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1};


CREATE TABLE shopping_elf.receipt_data
( userId TEXT,
  bill_date date,
  qty int,
  create_time date,
  product_name text,
  id text,
  PRIMARY KEY(id)
);


INSERT INTO shopping_elf.receipt_data (id,userId, bill_date1, qty,
   create_time, product_name) VALUES('1_B','2', '2017-02-01', 1, '2017-04-20','B');

   SELECT * FROM shopping_elf.receipt_data;


   create column family data
   with key_validation_class=Int32Type
   and comparator=DateType
   and default_validation_class=FloatType;
