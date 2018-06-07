#assign value 100 to variable cars
cars = 100
#assign value 4 to variable space_in_car
space_in_car = 4
#assign value 30 to variable drivers
drivers = 30
#assign value 90 to variable passengers
passengers = 90
#calculate the value of "cars - drivers" and assign it to "cars_not_driven"
cars_not_driven = cars - drivers
#assign value from "drivers" to variable "cars_driven"
cars_driven = drivers
#find the value of "cars_driven * space_in_car to variable passengers
carpool_capacity = cars_driven * space_in_car
#divide the value of "passengers" by the value of "cars_driven" and
#assign this value to "average_passengers_per_car"
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
        "in each car.")

#if you try to reference an undefined variable you will get a "NameError"
