
import MySQLdb
from Models import ShoppingItems
from Models import ShoppingList




db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="shopping")        # name of the data base

def getShoppingList(userid):
    cur = db.cursor()
    cur.execute("SELECT product_name,invoice_date,days FROM `inventory` WHERE  user_id ='%s'  and DATE_ADD(invoice_date,INTERVAL days DAY) > DATE_ADD(NOW(),INTERVAL 2 DAY)" %(userid))
    rows=cur.fetchall()
    shoppingList =[]
    for each_row in rows:
        shoppingList.append(ShoppingItems(each_row[0],each_row[1],each_row[2]));

    return ShoppingList(shoppingList);
