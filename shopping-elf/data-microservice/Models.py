
import collections

class ShoppingItems:
    productName= "";
    #quantity="";
    billDate = None;
    estimate_days = None;
    def __init__(self,productName, billDate,estimate_days):
        self.productName=productName
        #self.quantity = quantity;
        self.billDate= billDate;
        self.estimate_days=estimate_days;

class ShoppingList:
    shoppingItems = []
    def __init__(self,shoppingItems):
        self.shoppingItems=shoppingItems
