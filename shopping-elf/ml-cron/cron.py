from pcluster import pcluster
from Models import UserData
from Models import ProductData
from Models import Data
import uregression as uregression
import processed-data-service as pdservice
import clustering-regression as cregression

optimal_data =2

def calculate(allData,allProductData,allProducts):

    clusters = pcluster.cluster_texts(allProducts, 10);

    for eachUserData in allData.userData:
        for userProductData in eachUserData.productData:
            if(userProductData.length > optimal_data):

                // call first use case and save processed Data

                days = uregression.estimate_days(userProductData);

            else:
                 // get product cluster and all products of that cluster

                 cluster_products = pcluster.find_all_products(allProducts,clusters,userProductData.productName)
                 data = pdservice.getProductData(cluster_products);
                 // get data for those products
                 // call second multivariate script
                 //save Data if multiple products
                 days = cregression.estimate_days(productData)
