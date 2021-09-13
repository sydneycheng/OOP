import InsectClass as i

#this creates 2 diff instances
mosquito = i.Insect()
housefly = i.Insect()

mosquito.flight_length()

housefly.flight_length()

print("the mosquito can fly up to", mosquito.get_miles(), "miles")
print("the housefly can fly up to", housefly.get_miles(), "miles")


    