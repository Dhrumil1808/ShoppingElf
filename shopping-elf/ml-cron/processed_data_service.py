import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import time
import random
from datetime import datetime
import MySQLdb




db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="shopping")        # name of the data base

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)


#print i
# Use all the SQL you like
#cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
def saveData(processedData):
    cur = db.cursor()
    i=cur.rowcount;
    #with open("data/processed_data.txt","r") as text_file:
        #all_lines = text_file.read().split("\n")

    #lines= [line.split("|") for line in all_lines if ((len(line.split("|"))==3) and (line.split("|")[2]<> ''))]


#print len(product_qty);
#print len(all_lines)

    for eachData in processedData:
        #print index
        i=i+1
        user_id=eachData.userId
        #print user_id
        product_name=eachData.productName
        #print product_name
        invoice_date = eachData.billDate
        #print invoice_date
        days= eachData.estimate_days
        #print days
        cron_date = eachData.userId

        family_members= eachData.family_members
        #print cron_date
        #print "SELECT * FROM `inventory` WHERE user_id = '%s' AND product_name= '%s' " %(user_id) %(product_name)
        cur.execute("SELECT * FROM `inventory` WHERE user_id ='%s' AND product_name= '%s'" %(user_id,product_name))
        rows_update=cur.fetchall()
        #print len(rows_update)
        if(len(rows_update)==1):
            invoice_date_updated = datetime.strptime(invoice_date, "%Y-%m-%d").strftime('%Y-%m-%d')
            # print cron_date_updated
            cur.execute("UPDATE inventory SET invoice_date='%s',days= '%s',cron_date= '%s' WHERE user_id ='%s' AND product_name='%s'" %(invoice_date_updated,days,cron_date,user_id,product_name))
            db.commit()
        else:
            cur.execute("INSERT INTO `inventory`(user_id,product_name,invoice_date,days,cron_date,family_members) VALUES (%s,%s, STR_TO_DATE(%s,'%%Y-%%m-%%d'),%s,NOW(),%s)", (user_id,product_name,invoice_date,days,family_members))
            db.commit()


    db.close()



def getProductData(products):
    cur = db.cursor()
    cur.execute("SELECT * FROM `inventory` WHERE  product_name in (%s)" %(products))
    rows=cur.fetchall()
