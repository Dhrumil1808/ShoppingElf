
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



