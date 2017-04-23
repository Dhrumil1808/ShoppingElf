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

cur = db.cursor()

# Use all the SQL you like
#cur.execute("SELECT * FROM YOUR_TABLE_NAME")

# print all the first cell of all the rows

with open("data/processed_data.txt","r") as text_file:
    all_lines = text_file.read().split("\n")

lines= [line.split("|") for line in all_lines if ((len(line.split("|"))==3) and (line.split("|")[2]<> ''))]

i=0;
#print len(product_qty);
#print len(all_lines)

for index in range(1, len(all_lines)-1):
    print index
    i=i+1
    user_id=all_lines[index].split("|")[0]
    print user_id
    product_name=all_lines[index].split("|")[1]
    print product_name
    invoice_date = all_lines[index].split("|")[2]
    print invoice_date
    days= float(all_lines[index].split("|")[3])
    print days
    cron_date = all_lines[index].split("|")[4]
    print cron_date
    #print "INSERT INTO `inventory` (`id`,`product_name`,`invoice_date`,`days` ,`cron_date`) VALUES (NULL,product_name,invoice_date,days,cron_date)"
    cur.execute("INSERT INTO `inventory` VALUES (%s,%s,%s, STR_TO_DATE(%s,'%%m-%%d-%%Y'),%s,STR_TO_DATE(%s,'%%m/%%d/%%Y'))", (i,user_id,product_name,invoice_date,days,cron_date))
    db.commit()

db.close()

    
  