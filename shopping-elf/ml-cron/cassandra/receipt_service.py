from cassandra.cluster import Cluster

#cluster = Cluster(['192.168.0.1', '192.168.0.2'])
cluster = Cluster()
session = cluster.connect('shopping_elf')


def addUserReciept(billReceipt):
    for eachItem in billReceipt.billItems:

    session.execute(
    """
    INSERT INTO receipt_data (userid, bill_date, qty,
      time, product_name) VALUES( %(userId)s, %(bill_date)s, %(qty)s , %(time)s,%(product_name)s)
    """,
    {"userId": "rash", "bill_date": "2017-02-01",'qty': 1.3,'time': "2017-01-01", 'product_name': "abc"}
    )


#'SELECT * FROM receipt_data where userid='+userId+' order by product_name,bill_date asc'
def fetchAllReciepts(userId):
    query = "SELECT product_name,bill_date,qty FROM receipt_data where userid=\'" + str(userId)+"\' order by product_name,bill_date asc;";
    rows = session.execute(query)
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty

addUserReciept();
fetchAllReciepts("rash")
