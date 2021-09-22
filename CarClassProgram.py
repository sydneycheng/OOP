import CarClass

year_model = input("Enter your car's year and model: ")
make = input("Enter the make of your car: ")


car = CarClass.Car(year_model,make)

#calls the accelerator method 5 times
#get the current speed of the car after each call to the accelerator method
num = 5

for x in range(num):
    car.accelerate()
    car.get_speed()


#call the brake method 5 times
#get the current speed of the car after each call to the accelerator method
for s in range(num):
    car.brake()
    car.get_speed()
