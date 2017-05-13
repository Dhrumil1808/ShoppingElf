
import mysql.connector
from Models import ShoppingItems
from Models import ShoppingList
import collections
import DbConstants




def getShoppingList(userid):
    db = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                       database=DbConstants.DATABASE)
    cur = db.cursor()

    query = "SELECT product_name,DATE_FORMAT(invoice_date,'%%m-%%d-%%Y'),days,quantity,ABS(DATEDIFF(NOW(),DATE_ADD(invoice_date,INTERVAL days DAY))) as last FROM `inventory` WHERE  user_id ='%s' and (DATE_ADD(invoice_date,INTERVAL days DAY) < DATE_ADD(NOW(),INTERVAL 2 DAY) or DATE_ADD(invoice_date,INTERVAL days DAY) > DATE_ADD(NOW(),INTERVAL -2 DAY)) and ABS(DATEDIFF(NOW(),DATE_ADD(invoice_date,INTERVAL days DAY)))<7";

    cur.execute(query %(userid))
    rows=cur.fetchall()
    shoppingList =[]
    for each_row in rows:
        shoppingList.append(ShoppingItems(each_row[0],each_row[1],each_row[2],each_row[3],each_row[4]));
    cur.close()
    db.close()
    return formatShoppingData(shoppingList);

def getShoppingListProducts(userid):
    db = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                       database=DbConstants.DATABASE)
    cur = db.cursor()

    query = "SELECT product_name FROM `inventory` WHERE  user_id ='%s' and (DATE_ADD(invoice_date,INTERVAL days DAY) < DATE_ADD(NOW(),INTERVAL 2 DAY) or DATE_ADD(invoice_date,INTERVAL days DAY) > DATE_ADD(NOW(),INTERVAL -2 DAY)) and ABS(DATEDIFF(NOW(),DATE_ADD(invoice_date,INTERVAL days DAY)))<7";

    cur.execute(query %(userid))
    rows=cur.fetchall()
    shoppingList =[]
    for each_row in rows:
        shoppingList.append(each_row[0]);
    cur.close()
    db.close()
    return shoppingList;


def getProductConsumption(userid,product_name):
    db = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                       database=DbConstants.DATABASE)
    cur = db.cursor()

    query = "SELECT DATE_FORMAT(invoice_date,'%%m-%%d-%%Y'),bill_date, qty FROM shopping_elf.receipt_data where product_name='%s' and userid= '%s'"


    cur.execute(query %(userid,product_name) )
    rows=cur.fetchall()
    sList = [];
    for each_row in rows:
        d = collections.OrderedDict()
        d['date'] = each_row[0];
        d['quantity'] = each_row[1];
        sList.append(d)
    cur.close()
    db.close()
    return sList;


def getNotificationData():
    db = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                       database=DbConstants.DATABASE)
    cur = db.cursor()

    query = "select i.user_id,u.user_api_key, i.product_name from shopping_elf.inventory i , shopping_elf.`user` u where DATEDIFF(NOW(),invoice_date) +1 = days and u.username=i.user_id order by user_id"


    cur.execute(query)
    rows=cur.fetchall()
    notificationsList=collections.OrderedDict()

    for each_row in rows:

        if(each_row[1] in notificationsList):
            productList = notificationsList[each_row[1]]
            productList.append(each_row[2])
        else:
            productList=[]
            productList.append(each_row[2])
            notificationsList[each_row[1]] =productList

    cur.close()
    db.close()
    return notificationsList;



def formatShoppingData(shoppingList):
    sList =[];
    for eachData in shoppingList:
        d = collections.OrderedDict()
        d['productName'] = eachData.productName;  # its agent id
        d['lastBilldate'] = eachData.billDate;
        d['estimate_days'] = eachData.estimate_days;
        d['quantity'] = eachData.quantity;
        d['estimated_days_to_last'] = eachData.estimated_days_to_last;
        sList.append(d)

    return sList;



