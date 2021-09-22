
class Plant:    #superclass
    def __init__(self,color):   #only one attribute - color
        self.__color = color


    def get_color(self):    #only one method - get_color
        return self.__color


class Flower(Plant):        #FLOWER is a subclass of plant
    def __init__(self,color, petals):
        Plant.__init__(self,color)  #must initialize Plant

        self.__petals = petals  #petals only applies in the subtype, not the supertype

    def get_petals(self):
        return self.__petals
    
