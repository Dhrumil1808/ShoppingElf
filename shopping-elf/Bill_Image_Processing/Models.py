from flask import json
import collections

class BillReceipt:
    userId=None;
    billItems =[];
    billDate =None;
    def __init__(self,userId, billItems,billDate):
        self.userId=userId
        self.billItems = billItems;
        self.billDate=billDate;


class BillItem:
    productName= "";
    quantity="";
    def __init__(self,productName, quantity):
        self.productName=productName
        self.quantity = quantity;
