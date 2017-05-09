
import collections

class ShoppingItems:
    productName= "";
    quantity="";
    billDate = None;
    estimate_days = None;
    estimated_days_to_last =None
    def __init__(self,productName, billDate,estimate_days,quantity,estimated_days_to_last):
        self.productName=productName
        #self.quantity = quantity;
        self.billDate= billDate;
        self.estimate_days=estimate_days;
        self.quantity=quantity;
        self.estimated_days_to_last=estimated_days_to_last;

class ShoppingList:
    shoppingItems = []
    def __init__(self,shoppingItems):
        self.shoppingItems=shoppingItems
