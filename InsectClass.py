import random

class Insect:           #self: makes sure that we are only interacting w atributes of that instance
    def __init__(self,w,l): #short for "initialize"; always the first instance in a class method
        self.wings = w      #w and l are now variables
        self.legs = l
        self.flight = 0

    def flight_length(self):
        self.flight = random.randint(1,10)

    def get_miles(self): #get_miles is an accessor mutator (aka: it's a return statement of an attribute; mutator means changing the value of an attribute)
        return self.flight