class Phone:

#init method
    def __init__(self,manufacturer,model,retail_price):
        self.__manufact = mf
        self.__model = mdl 
        self.__retail_price = rp 
    
#set methods that accept arguments  
    def set_manufact(self, manufacturer):
        self.__manufact = manufacturer

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, retail_price):
        self.__retail_price = retail_price

#get methods
    def get_manufact(self):
        return self.__manufact 

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
    


