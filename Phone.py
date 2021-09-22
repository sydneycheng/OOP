import PhoneClass

def main():
    
    #Create a PhoneClass object
    

    mf = input("Enter the name of you cellphone's manufacturer: ")
    mdl = input("Enter you cellphone's model number: ")
    rp = float(input("Enter the retail price of your cellphone: "))
   
    cellphone = PhoneClass.Phone(mf,mdl,rp)

    print("Your cellphone information is up to date!\n")

    print("Manufacturer: ", mf)
    print("Model: ", mdl)
    print("Retail Price: $", rp)


main()