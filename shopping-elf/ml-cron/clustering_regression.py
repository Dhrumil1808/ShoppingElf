#!/usr/bin/python

"""
    Starter code for the regression mini-project.

    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""


import numpy as np

from datetime import datetime

from sklearn import linear_model

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)


def estimate_days(productData,testData,product_cluster):
    product_name=[]
    quantity=[]
    days=[]
    product_quantity_people=[]
    number_of_people=[]
    features_list=[]

    j = len(productData)-1
    #print j
    for i in range(0,j):
        product_name.append(product_cluster)

        if(i != j-1):
            days.append(productData[i].estimate_days)
            features_list.append([(float)(productData[i].quantity),(float)(productData[i].family_members)])


    #print days
    #print features_list

    days=np.array(days).reshape(len(days),1)

    regr = linear_model.LinearRegression()

    regr.fit(features_list, days)


    #print testData
    product_quantity_people.append([(float)(testData.quantity), (float)(testData.family_members)])

    #print product_quantity_people
    result=regr.predict(product_quantity_people)

    esitmated_days = 0;
    for it in result:
        for val in it:
            esitmated_days = int(result)

    #print esitmated_days
    return esitmated_days
