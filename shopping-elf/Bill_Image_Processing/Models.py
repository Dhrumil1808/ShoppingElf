from flask import json
import collections

class BillReceipt:
    userId=None;
    billItems =[];
    family_members=None;
    billDate =None;
    def __init__(self,userId, billItems,billDate,family_members):
        self.userId=userId
        self.billItems = billItems;
        self.billDate=billDate;
        self.family_members=family_members;


class BillItem:
    productName= "";
    quantity="";
    def __init__(self,productName, quantity):
        self.productName=productName
        self.quantity = quantity;


class User:
    userid =None
    username = "";
    family_members="";
    def __init__(self,userid,username, family_members):
        self.userid=userid
        self.username=username
        self.family_members = family_members;
