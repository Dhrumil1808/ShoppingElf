from cassandra.cluster import Cluster
from time import gmtime, strftime
from Models import BillReceipt
from Models import BillItem
from Models import User

cluster = Cluster()
session = cluster.connect('shopping_elf')

def getProducts():
    products =[];
    query = "SELECT product_name FROM products";
    rows = session.execute(query)
    for user_row in rows:
        products.append(user_row.product_name);
    return products;

def fetchAllReciepts(userId):
    query = "SELECT product_name,bill_date,qty FROM receipt_data where userid=\'" + str(userId)+"\' order by product_name,bill_date asc;";
    rows = session.execute(query)
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty


def fetchAllUserReciepts():
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
