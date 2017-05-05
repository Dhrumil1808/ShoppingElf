from pcluster import pcluster
from Models import UserData
from Models import ProductData


def calculate(allData):

    clusters = pcluster.cluster_texts(userProductData, 10);
    for eachUserData in allData.userData:
        for userProductData in eachUserData.productData:
            if(userProductData.length>2):

                // call first use case and save processed Data

            else:
                 // get product cluster and all products of that cluster
                 // get data for those products
                 // call second multivariate script
                 //save Data if multiple products
                 
