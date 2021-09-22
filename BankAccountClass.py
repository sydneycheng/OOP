# The BankAccount class simulates a bank account.

class BankAccount:
    

# The __init__ method accepts an argument for
# the account's balance. It is assigned to
# the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal #only one attribute; look at init to determine how many attributes in a Class

      # The deposit method makes a deposit into the
      # account.

    def deposit(self, amount): #deposit is a method
        self.__balance += amount

      # The withdraw method withdraws an amount
      # from the account.

    def withdraw(self, amount):
      if amount < 0:
        print("You cannot withdraw a negative amount.")
      else:
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Error: Insufficient funds')

      # The get_balance method returns the
      # account balance.

    def get_balance(self): #accessor method OR get method
        return self.__balance



    def __str__(self):
       return 'The balance is $' + format(self.__balance, ',.2f')
