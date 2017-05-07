
import collections

class UserData:
    userId=None;
    productData =[];
    def __init__(self,userId, productData):
        self.userId=userId
        self.productData = productData;


class ProductTuple:
    quantity="";
    billDate = None;
    family_members=None
    def __init__(self,quantity, billDate,family_members):
        self.quantity = quantity;
        self.billDate= billDate;
        self.family_members=family_members;

class ProductData:
    productName= "";
    quantity="";
    billDate = None;
    family_members=None
    def __init__(self,productName, quantity, billDate,family_members):
        self.productName=productName
        self.quantity = quantity;
        self.billDate= billDate;
        self.family_members=family_members;


class ProcessedData:
    userId=None
    productName= "";
    quantity="";
    billDate = None;
    estimate_days = None;
    family_members=None
    def __init__(self,userId,productName, quantity, billDate,family_members,estimate_days):
        self.userId=userId
        self.productName=productName
        self.quantity = quantity;
        self.billDate= billDate;
        self.family_members=family_members;
        self.estimate_days=estimate_days;




class Data:
    userData = [];
    def __init__(self,userData):
        self.userData=userData
