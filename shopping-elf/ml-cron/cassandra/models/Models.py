import mysql.connector
from flask import json
import collections

class BillReceipt:
    userId=None;
    billItems =[];
    bill_date =None;
    def __init__(userId, billItems):
        self.userId=userId
        self.billItems = billItems;


class BillItem:
    productName= "";
    quantity="";
    def __init__(productName, quantity):
        self.productName=productName
        self.quantity = quantity;
