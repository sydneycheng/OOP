import CarClass

year_model = input("Enter your car's year and model: ")
make = input("Enter the make of your car: ")


car = CarClass.Car(year_model,make)

#calls the accelerator method 5 times
#get the current speed of the car after each call to the accelerator method
num = 5

for x in range(num):
    print("Your car's current speed is: ")
    car.accelerate()
    print(car.get_speed())

#call the brake method 5 times
#get the current speed of the car after each call to the speed method

for s in range(num):
    print("Your car's current speed is: ")
    car.brake()
    print(car.get_speed())
