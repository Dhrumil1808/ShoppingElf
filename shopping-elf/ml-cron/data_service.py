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
        for user_row in rows:
            if str(user_row[0]) != '':
                if len(str(user_row[0]).strip(":?!\" ")) > 2:
                    products.append(str(user_row[0]));
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"

    return products;

def fetchAllReciepts(userId):

    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT product_name,bill_date,qty FROM receipt_data where userid=%s order by product_name,bill_date asc"""
        cursor.execute(query,(str(userId),))
        rows = cursor.fetchall()
        for user_row in rows:
            print user_row[1], user_row[0], user_row[2]
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"



def fetchAllUserReciepts():
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    user = {}
    try:
        query = """SELECT userid,product_name,bill_date,qty,family_members FROM receipt_data order by userid,product_name,bill_date asc"""
        cursor.execute(query)
        rows = cursor.fetchall()
        user = {}
        for user_row in rows:
            if (user_row[0] in user):
                productdata = user[user_row[0]];
                if (user_row[1] in productdata):
                    eachProductBillData = productdata[user_row[1]]
                    eachProductBillData.append(ProductTuple(user_row[3],
                                                            user_row[2], user_row[4]));
                else:
                    productBillData = []
                    productBillData.append(ProductTuple(user_row[3], user_row[2], user_row[4]));
                    productdata[user_row[1]] = productBillData
            else:
                productdata = {}
                tuplelist = []
                tuplelist.append(ProductTuple(user_row[3],
                                              user_row[2], user_row[4]));
                productdata[user_row[1]] = tuplelist;
                user[user_row[0]] = productdata;
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"
    return user


def findUser(username):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST, database=DbConstants.DATABASE)
    cursor = database.cursor()
    try:
        query = """SELECT userid,family_members,username  FROM user where username=%s"""
        cursor.execute(query,(str(username)))
        rows = cursor.fetchall()
        for user_row in rows:
            user = User(user_row[0], user_row[2], user_row[1]);
    except mysql.connector.Error as err:
        cursor.close()
        database.close()
        return "err"

    return user;




def testfetch():
    fetchAllUserReciepts();


