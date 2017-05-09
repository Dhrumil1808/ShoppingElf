
import MySQLdb
from Models import ShoppingItems
from Models import ShoppingList
import collections




db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="shopping_elf")        # name of the data base


def getShoppingList(userid):
    cur = db.cursor()


    cur.execute("SELECT product_name,DATE_FORMAT(invoice_date,'%%d-%%m-%%Y'),days,quantity FROM `inventory` WHERE  user_id ='%s'  and DATE_ADD(invoice_date,INTERVAL days DAY) > DATE_ADD(NOW(),INTERVAL 2 DAY)" %(userid))
    rows=cur.fetchall()
    shoppingList =[]
    for each_row in rows:
        shoppingList.append(ShoppingItems(each_row[0],each_row[1],each_row[2],each_row[3]));


    return formatShoppingData(shoppingList);


def formatShoppingData(shoppingList):
    sList =[];
    for eachData in shoppingList:
        d = collections.OrderedDict()
        d['productName'] = eachData.productName;  # its agent id
        d['lastBilldate'] = eachData.billDate;
        d['estimate_days'] = eachData.estimate_days;
        d['quantity'] = eachData.quantity;

        sList.append(d)

    return sList;



