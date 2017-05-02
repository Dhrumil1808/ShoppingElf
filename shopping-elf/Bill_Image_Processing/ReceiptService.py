from cassandra.cluster import Cluster
from time import gmtime, strftime
from Models import BillReceipt
from Models import BillItem

cluster = Cluster(['10.0.0.98'])
session = cluster.connect('shopping_elf')

def addUserReciept(billReceipt):
    bill_date= billReceipt.billDate;
    user_id= billReceipt.userId;
    print user_id
    currentDate= strftime("%Y-%m-%d", gmtime())

    for eachItem in billReceipt.billItems:
        session.execute(
        """
        INSERT INTO receipt_data (userid, bill_date, qty,
        time, product_name) VALUES( %(userId)s, %(bill_date)s, %(qty)s , %(time)s,%(product_name)s)
        """,
        {"userId": user_id, "bill_date": bill_date,'qty': eachItem.quantity,'time': currentDate, 'product_name': eachItem.productName}
        )




def fetchAllReciepts(userId):
    query = "SELECT product_name,bill_date,qty FROM receipt_data where userid=\'" + str(userId)+"\' order by product_name,bill_date asc;";
    rows = session.execute(query)
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty


def testAdd():

    billItem = BillItem ("sample_product",10);
    items =[];
    items.append(billItem);
    billReceipt = BillReceipt ("rash",items,"2017-01-01");
    addUserReciept(billReceipt);
    fetchAllReciepts("rash")
