import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import time
import random
from datetime import datetime
import mysql.connector
import DbConstants

from Models import ProcessedData;


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)


#print i
# Use all the SQL you like
#cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows
def saveData(processedData):


    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                       database=DbConstants.DATABASE)
    cur = database.cursor()
    i=cur.rowcount;

    for eachData in processedData:
        #print index
        i=i+1
        user_id=eachData.userId
        #print user_id
        product_name=eachData.productName
        #print product_name
        invoice_date = str(eachData.billDate)
        #print invoice_date
        days= eachData.estimate_days
        #print days

        quantity= eachData.quantity

        family_members= eachData.family_members
        #print cron_date
        #print "SELECT * FROM `inventory` WHERE user_id = '%s' AND product_name= '%s' " %(user_id) %(product_name)
        try:
            cur.execute("SELECT * FROM `inventory` WHERE user_id ='%s' AND product_name= '%s'" %(user_id,product_name))
            rows_update=cur.fetchall()
            #print len(rows_update)
            if(len(rows_update)==1):
                invoice_date_updated = datetime.strptime(invoice_date, "%Y-%m-%d").strftime('%Y-%m-%d')
                print invoice_date_updated
                # print cron_date_updated
                cur.execute("UPDATE inventory SET invoice_date='%s',days= '%s',cron_date= NOW(),quantity='%s' WHERE user_id ='%s' AND product_name='%s' " %(invoice_date_updated,days,quantity,user_id,product_name))
                database.commit(),
            else:
                cur.execute("INSERT INTO `inventory`(user_id,product_name,invoice_date,days,cron_date,family_members,quantity) VALUES (%s,%s,%s,%s,NOW(),%s,%s)", (user_id,product_name,invoice_date,days,family_members,quantity))
                database.commit()
        except mysql.connector.Error as err:
            print("In Data saving : Something went wrong: {}".format(err))

    database.close()




def getProductData(products):
    database = mysql.connector.connect(user=DbConstants.USER, passwd=DbConstants.PASSWORD, host=DbConstants.HOST,
                                       database=DbConstants.DATABASE)
    ProductList =[]
    pdStr= "";
    size =len(products)
    i=1;
    for product in products:
       pdStr= pdStr+ "'"+product+"'"
       if(i!=size):
            pdStr = pdStr +","
       i=i+1;

    print pdStr
    try:
        cur = database.cursor()
        query ="SELECT product_name,days,family_members,quantity,days FROM `inventory` WHERE  product_name in ("+pdStr+")"
        print query
        cur.execute(query);
        rows=cur.fetchall()
        for r in rows:
            ProductList.append(ProcessedData("A",r[0], r[3], "",r[2],r[4]))

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        database.close()
    return ProductList
