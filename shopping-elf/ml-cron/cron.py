
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

    #clusters = pcluster.cluster_texts(allProducts, 10);
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
                    #days = 1;
                    processedData.append(ProcessedData(user,product, last_bill.quantity, last_bill.billDate,last_bill.family_members,days))
                else:
                    if (user in noHistoryData):
                        productdata = noHistoryData[user];
                        if(product not in productdata):
                            productdata[product] =userProductData
                    else:
                        productdata ={}
                        tuplelist=[]
                        tuplelist.append(userProductData);
                        productdata[product]=tuplelist;
                        noHistoryData[user]= productdata;
    print  "####################################################"

    pdservice.saveData(processedData)


def cluster_estimates(noHistoryData,products):
        #for eachNoHistoryData in noHistoryData:
            #cluster_products = pcluster.find_all_products(allProducts,clusters,userProductData.productName)
            #data = pdservice.getProductData(cluster_products);
            #days = cregression.estimate_days(productData)

    return 0

products = dservice.getProducts();
allData = dservice.fetchAllUserReciepts();

#print allData
calculate(allData,products);
