
import collections

class UserData:
    userId=None;
    productData =[];
    def __init__(self,userId, productData):
        self.userId=userId
        self.productData = productData;


class ProductData:
    productName= "";
    quantity="";
    billDate = None;
    def __init__(self,productName, quantity, billDate):
        self.productName=productName
        self.quantity = quantity;
        self.billDate= billDate;


class ClusterProductData:
    productName= "";
    quantity="";
    billDate = None;
    family_members=None
    def __init__(self,productName, quantity, billDate):
        self.productName=productName
        self.quantity = quantity;
        self.billDate= billDate;
        self.family_members=family_members;


class Data:
    userData = [];
    def __init__(self,userData):
        self.userData=userData
