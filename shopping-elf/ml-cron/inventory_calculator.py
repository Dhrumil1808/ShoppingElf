
# coding: utf-8

# In[1]:

#get_ipython().magic(u'matplotlib inline')


# 
# # Linear Regression Example
# 
# This example uses the only the first feature of the `diabetes` dataset, in
# order to illustrate a two-dimensional plot of this regression technique. The
# straight line can be seen in the plot, showing how linear regression attempts
# to draw a straight line that will best minimize the residual sum of squares
# between the observed responses in the dataset, and the responses predicted by
# the linear approximation.
# 
# The coefficients, the residual sum of squares and the variance score are also
# calculated.
# 
# 

# In[ ]:




# In[5]:

print(__doc__)
# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import time
import random
from datetime import datetime
import MySQLdb
import arrow

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="shopping")        # name of the data base

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)

with open("data/user-product-sample.txt","r") as text_file:
    all_lines = text_file.read().split("\n")

lines= [line.split("|") for line in all_lines if ((len(line.split("|"))==3) and (line.split("|")[2]<> ''))]

product_qty_array= [(float(line[2])) for line in lines]

#print len(product_qty);
#print len(all_lines)
product_name_array=[line[0] for line in lines]
product_name_test=product_name_array.pop(len(product_name_array)-1)

output=[]
#print len(all_lines)
i=1;
days_array=[]
products_array=[]
j=0;
prev=0;
print len(all_lines)
for index in range(1, len(all_lines)):
    product_name=all_lines[index-1].split("|")[0]
    product_name_next=all_lines[index].split("|")[0]
    previous_date= all_lines[index-1].split("|")[1]
    next_date=all_lines[index].split("|")[1]
    qty= float(all_lines[index-1].split("|")[2])
    qty_latest=float(all_lines[index].split("|")[2])
    
    #condition runs for the last entry in the database
    if(index==len(all_lines)-1):
        qty_array=[]
        days=np.array(days_array);
        products=np.array(products_array).reshape(len(products_array),1)
        #print days
        days_test=np.array(random.sample(range(1,30),len(days_array)-1))
        
        #print days_test
        qty_array.append(qty_latest)
        
        qty_latest1=np.array(qty_array).reshape(1,1)
        print qty_latest1
        #print days_test
        # Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(products, days)

        # The coefficients
        #print('Coefficients: \n', regr.coef_)
        prediction=regr.predict(float(qty_latest))
        #print prediction
        
        
        with open("data/processed_data.txt","a") as write_file:
            write_file.write("\n")
            write_file.write("1")
            write_file.write("|")
            write_file.write(product_name)
            write_file.write("|")
            write_file.write(next_date)
            write_file.write("|")
            write_file.write('%d' % int(prediction))
            write_file.write("|")
            write_file.write(arrow.now().format('YYYY-MM-DD'))
            
    #condition runs for the same product with different bill date
    if(product_name==product_name_next):
        if(prev!=j and index!=1):
            del days_array[:]
            del products_array[:]
        prev=j;   
        d=days_between(next_date,previous_date)
        #print d
        days_array.append(d)
        products_array.append(qty)
        
        #condition runs when list of one product ends and the other starts 
    elif(product_name != product_name_next):
        qty_array=[]
        days=np.array(days_array);
        products=np.array(products_array).reshape(len(products_array),1)
        product_qty_test=np.array(random.sample(range(1,30),len(products))).reshape(len(products),1)
        days_test=np.array(random.sample(range(1,30),len(days_array)-1))
        qty_array.append(qty)
        qty_latest1=np.array(qty_array).reshape(1,1)
        print qty_latest1
        
        # Create linear regression object
        regr = linear_model.LinearRegression()

        # Train the model using the training sets
        regr.fit(products, days)

        # The coefficients
        #print('Coefficients: \n', regr.coef_)
        prediction=regr.predict(float(qty_latest1))
        #print prediction
        
        with open("data/processed_data.txt","a") as write_file:
            write_file.write("\n")
            write_file.write("1")
            write_file.write("|")
            write_file.write(product_name)
            write_file.write("|")
            write_file.write(previous_date)
            write_file.write("|")
            write_file.write('%d' % int(prediction))
            write_file.write("|")
            write_file.write(arrow.now().format('YYYY-MM-DD'))
        
        # The mean squared error
       # print("Mean squared error: %.2f"
        #         % np.mean((regr.predict(product_qty_test) - days_test) ** 2))
        # Explained variance score: 1 is perfect prediction
        # print('Variance score: %.2f' % regr.score(product_qty_test, days_test))

        # Plot outputs
        #plt.scatter(product_qty_test, days_test,  color='black')
        #plt.plot(product_qty_test, regr.predict(product_qty_test), color='blue',linewidth=3)
        #plt.xticks(())
        #plt.yticks(())
        #plt.show()
                       


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



