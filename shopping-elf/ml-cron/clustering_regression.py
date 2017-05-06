#!/usr/bin/python

"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""    
import sys
import pickle
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import time
import random
from datetime import datetime
import MySQLdb
import arrow
from sklearn import linear_model
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
#import statsmodels.api as sm
sys.path.append("../tools/")
#from feature_format import featureFormat, targetFeatureSplit
#dictionary = pickle.load( open("data/sample.txt", "r") )

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%m-%d-%Y")
    d2 = datetime.strptime(d2, "%m-%d-%Y")
    return abs((d2 - d1).days)

productData=[['A','2','01-25-2017','3'],['A','12','01-28-2017','3'],['A','12','01-28-2017','3'],['A','5','02-15-2017','3'],['A','10','02-28-2017','3'],['A','1','03-05-2017','3'],['A','6','03-06-2017','3'],['A','10','03-16-2017','3'],['A','3','04-01-2017','1'],['A','8','04-03-2017','2'],['A','5','04-08-2017','4']]

### list the features you want to look at--first item in the 
### list will be the "target" feature
#features_list = ["category","quantity", "persons"]
#data = featureFormat( dictionary, features_list, remove_any_zeroes=True)
#target, features = targetFeatureSplit(data)
def estimate_days(productData):
    product_name=[]
    quantity=[]
    days=[]
    product_quantity_people=[]
    number_of_people=[]
    features_list=[]

    j = len(productData)-1 
    #print j   
    for i in range(0,j):
        product_name.append(productData[i][0])
        billDate=productData[i][2]
        if(i != j-1):
            billDate_next=productData[i+1][2]
            day=days_between(billDate,billDate_next)
            days.append(day)
            features_list.append([(float)(productData[i][1]),(float)(productData[i][3])])




        # The coefficients
        #print('Coefficients: \n', regr.coef_)
    #quantity=np.array(quantity).reshape(len(quantity),1)
    days=np.array(days).reshape(len(days),1)
    #number_of_people=np.array(number_of_people).reshape(len(number_of_people),1)



    regr = linear_model.LinearRegression()

        # Train the model using the training sets
    regr.fit(features_list, days)

    for i in  range(j,len(productData)):
        product_quantity_people.append([(float)(productData[i][1]),(float)(productData[i][3])])

    
    result=regr.predict(product_quantity_people)
    return result


output=estimate_days(productData)
print map(int,output)


def old_regression():

    with open("data/sample.txt","r") as text_file:
        all_lines = text_file.read().split("\n")

    lines= [line.split(" ") for line in all_lines if ((len(line.split(" "))==3) and (line.split(" ")[2]<> ''))]

    product_qty= [(line[0]) for line in lines]
    number_of_people= [(line[1]) for line in lines]
    number_of_days= [(line[2]) for line in lines]

    features_list=[]
    target=[]
#print (int) (len(all_lines) * 0.75)
    for i in range(0,(int)(len(all_lines) * 0.75)):
	   features_list.append([product_qty[i],number_of_people[i]])

    for j in range(0,(int)(len(all_lines) * 0.75)):
	   target.append([number_of_days[j]])	


    feature_train=np.array(features_list).astype(np.float)
    print feature_train
#feature_train=features_list.reshape(len(features_list),1)
### training-testing split needed in regression, just like classification
#target=np.array(target,np.float32).reshape(1,len(target))
    target=np.array(target).astype(np.float)
#print target
    target_train=target.reshape(len(feature_train),1)

    feature_test=[];
    target_test=[]

#print (int) ((len(all_lines)*0.75))
#print len(all_lines)
    for i in range((int)((len(all_lines)*0.75)),len(all_lines)-1):
	   feature_test.append([product_qty[i],number_of_people[i]])

    for i in range((int)((len(all_lines)*0.75)),len(all_lines)-1):
	   target_test.append([number_of_days[i]])	


#from sklearn.cross_validation import train_test_split
#feature_train, feature_test, target_train, target_test = train_test_split(features_list, target, test_size=0.25, random_state=42)
#train_color = "b"
#test_color = "r"

    feature_test=np.array(feature_test).astype(np.float)
    target_test=np.array(target_test).astype(np.float)
    print feature_test
#target_test=target_test
    target_test=target_test.reshape(len(feature_test),1)

    print target_test
#def reg_m(target, features_list):
 #   ones = np.ones(len(x[0]))
  #  X = sm.add_constant(np.column_stack((x[0], ones)))
   # for ele in x[1:]:
    #    X = sm.add_constant(np.column_stack((ele, X)))
    #results = sm.OLS(y, X).fit()
    #return results
### Your regression goes here!
### Please name it reg, so that the plotting code below picks it up and 
### plots it correctly. Don't forget to change the test_color above from "b" to
### "r" to differentiate training points from test points.

#print reg_m(target,features_list).summary()

#import multipolyfit.multipolyfit as mpf
    reg = linear_model.LinearRegression()
    reg.fit(feature_train,target_train)
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
#print reg.coef_
#print reg.intercept_
    print reg.score(feature_train,target_train)
    print reg.score(feature_test,target_test)
    for i in range(0,len(feature_test)):
	   print "prediction=", (int) (reg.predict(feature_test)[i])


#feature_test=feature_test.reshape(len(feature_test),1)
#target_test=target_test.reshape(2,len(feature_test))

    print np.shape(feature_test)
    print np.shape(target_test)
    print np.shape(feature_train)
    print np.shape(target_train)

#np.polyfit(feature_test, target_test, 1, rcond=None, full=False, w=None, cov=False)
#print accuracy_score(target_test,reg.predict(feature_test))
### draw the scatterplot, with color-coded training and testing pointsnp.a

    feature_test_scatter=np.array(feature_test).ravel()
    feature_train_scatter=np.array(feature_train).ravel()

    for feature, target in zip(feature_test_scatter,target_test):
        plt.scatter(feature,target,color="r") 
    for feature, target in zip(feature_train_scatter, target_train):
        plt.scatter(feature,target,color="b") 

### labels for the legend
    plt.scatter(feature_test_scatter[0], target_test[0], color="r", label="test")
    plt.scatter(feature_train_scatter[0], target_train[0], color="b", label="train")

#reg.fit(feature_test, target_test)
### draw the regression line, once it's coded
    try:
	   plt.plot(feature_test, reg.predict(feature_test))
    except NameError:
        pass
#print reg.coef_
    plt.plot(feature_train, reg.predict(feature_train)) 
    plt.xlabel("")
    plt.ylabel("")
    plt.legend()
    plt.show()
