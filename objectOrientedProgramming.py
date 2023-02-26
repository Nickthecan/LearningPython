#If the program is small, you can create object classes in the main file
#Otherwise, we would create a new file for just the classes
#you would need to import the file into the main file

from car import Car

""" class Car:
    pass """

#in order to create an object, we need to pass the same amount of arguments into the instantiation
car_1 = Car("Honda", "Civic", 2021, "Gray")

car_2 = Car("Ford", "Mustang", 2022, "Red")

car_3 = Car("Motorcycle", "Motorcycle", 2020, "Black")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("-------------------------------")
car_1.drive()
car_1.stop()
print("-------------------------------")
print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)
print("-------------------------------")
car_2.drive()
car_2.stop()
print("-------------------------------")
#One way to change a class variable
car_3.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
print(car_3.wheels)

#This changes the class variable for all cars
Car.wheels = 2