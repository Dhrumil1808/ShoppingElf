from cassandra.cluster import Cluster
from time import gmtime, strftime
from Models import BillReceipt
from Models import BillItem
from Models import User

cluster = Cluster()
session = cluster.connect('shopping_elf')

def addUserReciept(billReceipt):
    bill_date= billReceipt.billDate;
    user_id= billReceipt.userId;
    family_members = billReceipt.family_members;
    print user_id
    print family_members
    currentDate= strftime("%Y-%m-%d", gmtime())

    for eachItem in billReceipt.billItems:
        session.execute(
        """
        INSERT INTO receipt_data (userid, bill_date, qty,
        time, product_name, family_members) VALUES( %(userId)s, %(bill_date)s, %(qty)s , %(time)s,%(product_name)s , %(family_members)s)
        """,
        {"userId": user_id, "bill_date": bill_date,'qty': eachItem.quantity,'time': currentDate, 'product_name': eachItem.productName,'family_members':family_members}
        )

def addProducts(products):
    for eachProduct in products:
        session.execute(
        """
        INSERT INTO products (product_name) VALUES( %(product_name)s)
        """,
        {"product_name": eachProduct})


def fetchAllReciepts(userId):
    query = "SELECT product_name,bill_date,qty FROM receipt_data where userid=\'" + str(userId)+"\' order by product_name,bill_date asc;";
    rows = session.execute(query)
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty


def findUser(username):
    query = "SELECT userid,family_members,username  FROM user where username=\'" + str(username)+"\'";
    rows = session.execute(query)
    for user_row in rows:
        user = User(user_row.userid,user_row.username,user_row.family_members);
    return user;


def testAdd():
    billItem = BillItem ("sample_product",10);
    items =[];
    items.append(billItem);
    billReceipt = BillReceipt ("rash",items,"2017-01-01");
    addUserReciept(billReceipt);
    fetchAllReciepts("rash")
