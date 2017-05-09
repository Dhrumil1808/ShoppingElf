
from Models import UserData
from Models import ProductData
from Models import Data
from Models import ProcessedData
import uregression as uregression
import processed_data_service as pdservice
import clustering_regression as cregression
import data_service as dservice
import pcluster as pcluster


optimal_data =2



def calculate(allData,allProducts):
    print allProducts
    clusters = pcluster.cluster_texts(allProducts);
    processedData = [];
    noHistoryData={}

    for user,userData in allData.items():
        for product,userProductData in userData.items():

                if(len(userProductData) > optimal_data):
                #call first use case and save processed Data
                    days = uregression.estimate_days(userProductData,product);
                    print days
                    print product
                    last_bill = userProductData[len(userProductData)-1]

                    processedData.append(ProcessedData(user,product, last_bill.quantity, last_bill.billDate,last_bill.family_members,days))
                else:
                    if (user in noHistoryData):
                        productdata = noHistoryData[user];
                        if(product not in productdata):
                            productdata[product] =userProductData
                    else:
                        productdata ={}
                        productdata[product]=userProductData;
                        noHistoryData[user]= productdata;


    pdservice.saveData(processedData)

    cluster_estimates(clusters,noHistoryData,allProducts)




def cluster_estimates(clusters,noHistoryData,allProducts):
    processedData = [];

    for user,eachNoHistoryData in noHistoryData.items():
            for product,eachNoHistoryProduct in eachNoHistoryData.items():
                print eachNoHistoryProduct
                last_bill = eachNoHistoryProduct[len(eachNoHistoryProduct)-1]
                print "********#@$@@@@@@@@@@@@@@@@@@@"
                print last_bill
                cluster_products = pcluster.find_all_products(allProducts,clusters,product)
                if len(cluster_products)>=1:
                    print cluster_products
                    data = pdservice.getProductData(cluster_products);
                    print data
                    if(len(data)>optimal_data):
                        days = cregression.estimate_days(data,last_bill,"cluster_product")
                        processedData.append(
                        ProcessedData(user, product, last_bill.quantity, last_bill.billDate, last_bill.family_members,
                                  days))

    pdservice.saveData(processedData)




products = dservice.getProducts();
allData = dservice.fetchAllUserReciepts();

#print allData
calculate(allData,products);
