class RetailItem:

#init method
    def __init__(self,description,inventory,price):
        self.__description = description
        self.__units_inventory = inventory
        self.__price = price



#get methods
    def get_description(self):
        return self.__description

    def get_inventory(self):
        return self.__units_inventory

    def get_price(self):
        return self.__price



