
from Models import ProcessedData
import uregression as uregression
import processed_data_service as pdservice
import clustering_regression as cregression
import data_service as dservice
import pcluster as pcluster


optimal_data =2



def calculate(allData,allProducts):
    clusters = pcluster.cluster_texts(allProducts);
    processedData = [];
    noHistoryData={}
    print "calculating per user history"
    for user,userData in allData.items():
        for product,userProductData in userData.items():

                if(len(userProductData) > optimal_data):
                    days = uregression.estimate_days(userProductData,product);

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
    print "calculating per all user history"

    for user,eachNoHistoryData in noHistoryData.items():
            for product,eachNoHistoryProduct in eachNoHistoryData.items():
                last_bill = eachNoHistoryProduct[len(eachNoHistoryProduct)-1]
                cluster_products = pcluster.find_all_products(allProducts,clusters,product)
                if len(cluster_products)>=1:
                    data = pdservice.getProductData(cluster_products);
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
