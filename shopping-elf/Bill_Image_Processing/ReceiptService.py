from cassandra.cluster import Cluster
from time import gmtime, strftime
from Models import BillReceipt
from Models import BillItem
from Models import User
import mysql.connector
import DbConstants

def addUserReciept(billReceipt):
    print "adding user recipt"
    bill_date= billReceipt.billDate;
    user_id= billReceipt.userId;
    family_members = billReceipt.family_members;
    print user_id
    print family_members
    currentDate= strftime("%Y-%m-%d", gmtime())
    print "adding"
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    for eachItem in billReceipt.billItems:
        try:
            query = """INSERT INTO receipt_data (userid,bill_date,qty,time, product_name, family_members) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(query, (user_id,bill_date, eachItem.quantity, currentDate, eachItem.productName, family_members))
        except mysql.connector.Error as err:
            print "Something went wrong: {}" + format(err)
    database.commit()
    cursor.close()
    database.close()
    return "successful insert"

def addProducts(products):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()

    for eachProduct in products:
        query = """INSERT INTO products (product_name) VALUES (%s)"""
        try:
            cursor.execute(query, (eachProduct,))
            database.commit();
        except mysql.connector.Error as err:
            print "Something went wrong: {}"+format(err)
    cursor.close()
    database.close()
    return "successful insert"

def fetchAllReciepts(userId):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT product_name,bill_date,qty FROM receipt_data where userid = %s order by product_name,bill_date asc"""
        cursor.execute(query,(userid))
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty

def findUser(username):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT userid,family_members,username FROM user where username= %s """
        cursor.execute(query,(username,))
        rows = cursor.fetchall()
        print rows
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
    for user_row in rows:
        userid = user_row[0]
        username = user_row[2]
        family_members = user_row[1]
        user = User(userid,username,family_members);
    return user;

def testAdd():
    billItem = BillItem ("sample_product",10);
    items =[];
    items.append(billItem);
    billReceipt = BillReceipt ("rash",items,"2017-01-01");
    addUserReciept(billReceipt);
    fetchAllReciepts("rash")
