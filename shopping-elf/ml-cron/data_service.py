#from cassandra.cluster import Cluster
from time import gmtime, strftime
from Models import UserData
from Models import ProductData
from Models import ProductTuple
import mysql.connector
import DbConstants

# cluster = Cluster()
# session = cluster.connect('shopping_elf')

def getProducts():
    products =[];
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT product_name FROM products"""
        cursor.execute(query)
        rows = cursor.fetchall()
        print rows
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
    for user_row in rows:
        if str(user_row.product_name) != '':
            if len(str(user_row.product_name).strip(":?!\" ")) >2:
                products.append(str(user_row.product_name));
    print "*****************************************"
    print products
    return products;

def fetchAllReciepts(userId):

    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT product_name,bill_date,qty FROM receipt_data where userid=%s order by product_name,bill_date asc"""
        cursor.execute(query,(str(userid),))
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty


def fetchAllUserReciepts():
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT userid,product_name,bill_date,qty,family_members FROM receipt_data"""
        cursor.execute(query)
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
    user ={}
    for user_row in rows:
        if(user_row.userid in user):
            productdata = user[user_row.userid];
            if(user_row.product_name in productdata):
                eachProductBillData = productdata[user_row.product_name]
                eachProductBillData.append(ProductTuple(user_row.qty,
                user_row.bill_date,user_row.family_members));
            else:
                productBillData =[]
                productBillData.append(ProductTuple(user_row.qty,user_row.bill_date,user_row.family_members));
                productdata[user_row.product_name] =productBillData
        else:
            productdata ={}
            tuplelist=[]
            tuplelist.append(ProductTuple(user_row.qty,
            user_row.bill_date,user_row.family_members));
            productdata[user_row.product_name]=tuplelist;
            user[user_row.userid]= productdata;
    print user
    return user


def findUser(username):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT userid,family_members,username  FROM user where username=%s"""
        cursor.execute(query,(str(username)))
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
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

def testfetch():
    fetchAllUserReciepts();


testfetch()
