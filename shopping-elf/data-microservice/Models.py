
import collections

class ShoppingItems:
    productName= "";
    quantity="";
    billDate = None;
    estimate_days = None;
    def __init__(self,productName, billDate,estimate_days,quantity):
        self.productName=productName
        #self.quantity = quantity;
        self.billDate= billDate;
        self.estimate_days=estimate_days;
        self.quantity=quantity;

class ShoppingList:
    shoppingItems = []
    def __init__(self,shoppingItems):
        self.shoppingItems=shoppingItems
