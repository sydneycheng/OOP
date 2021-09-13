import random

# The Coin class simulates a coin that can
# be flipped.


#"Coin" is the name of the class
class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

                        #this will always be the first method
    def __init__(self): #every coin we create is initialized with 'heads'
        self.sideup = 'Heads'

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'

    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):
            return self.sideup
