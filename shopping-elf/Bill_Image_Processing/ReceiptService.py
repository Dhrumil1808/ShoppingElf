from cassandra.cluster import Cluster
from time import gmtime, strftime
from Models import BillReceipt
from Models import BillItem
from Models import User
import mysql.connector

# cluster = Cluster()
# session = cluster.connect('shopping_elf')
database=None

def addUserReciept(billReceipt):
    bill_date= billReceipt.billDate;
    user_id= billReceipt.userId;
    family_members = billReceipt.family_members;
    print user_id
    print family_members
    currentDate= strftime("%Y-%m-%d", gmtime())
    
    self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = self.database.cursor()
    for eachItem in billReceipt.billItems:
        query = """INSERT INTO receipt_data (userid,bill_date,qty,time, product_name, family_members) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query, (self.user_id,self.bill_date, self.qty, self.time, self.product_name, self.family_members))
        self.database.commit()
        cursor.close()
        self.database.close()
        return result

def addProducts(products):
    self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = self.database.cursor()

    for eachProduct in products:
        query = """INSERT INTO products (product_name) VALUES (%s)"""
        cursor.execute(query, (self.eachProduct))
        self.database.commit()
        cursor.close()
        self.database.close()
        return result

def fetchAllReciepts(userId):
    self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = self.database.cursor()
    try:
        query = """SELECT product_name,bill_date,qty FROM receipt_data where userid = %s order by product_name,bill_date asc"""
        cursor.execute(query,(self.userid))
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        cursor.close()
        self.database.close()
        return "err"
    for user_row in rows:
        print user_row.bill_date, user_row.product_name, user_row.qty

def findUser(username):
    self.database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = self.database.cursor()
    try:
        query = """SELECT userid,family_members,username  FROM user where username= %s """
        cursor.execute(query,(self.userid))
        rows = cursor.fetchall()
    except mysql.connector.Error as err:
        cursor.close()
        self.database.close()
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
