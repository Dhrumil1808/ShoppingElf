

import numpy as np
from sklearn import datasets, linear_model

from datetime import datetime




def days_between(d1, d2):

    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)




def estimate_days(productData, name):
    product_name=[]
    quantity=[]
    days=[]
    product_quantity=[]
    j = len(productData)-1
    for i in range(0,j):
        product_name.append(name)
        billDate=productData[i].billDate
        if(i != j-1):
            billDate_next=productData[i+1].billDate
            day=days_between(str(billDate),str(billDate_next))
            days.append(day)
            quantity.append((float) (productData[i].quantity))


        # The coefficients
        #print('Coefficients: \n', regr.coef_)
    quantity=np.array(quantity).reshape(len(quantity),1)
    days=np.array(days).reshape(len(days),1)

    regr = linear_model.LinearRegression()

        # Train the model using the training sets
    regr.fit(quantity, days)

    for i in  range(j,len(productData)):
        product_quantity.append((float)(productData[i].quantity))

    product_quantity=np.array(product_quantity).reshape(len(product_quantity),1)
    result=regr.predict(product_quantity)
    esitmated_days =0;
    for it in result:
        for val in it:
            esitmated_days =  int(val)

    return esitmated_days

