# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item) 
#there is a better way to write this
print("--------------------------------------------------")
#can use placeholders {} and then use the format method
print("The {} jumped over the {}".format("cow", "moon"))
print("The {} jumped over the {}".format(animal, item))
#using positional arguments
print("--------------------------------------------------")
print("The {0} jumped over the {1}".format("cow", "moon"))
print("The {1} jumped over the {0}".format("cow", "moon"))
#using keyword arguments
print("--------------------------------------------------")
print("The {animal2} jumped over the {item2}".format(animal2 = "COW", item2 = "MOON"))
print("The {item2} jumped over the {item2}".format(animal2 = "COW", item2 = "MOON"))
print("The {item2} jumped over the {animal2}".format(animal2 = "COW", item2 = "MOON"))
print("The {animal2} jumped over the {animal2}".format(animal2 = "COW", item2 = "MOON"))

print("===========================================================================")
#using padding in the format method
name = "Anna"

print("Hello, my name is {}. Nice to meet you !".format(name))
print("Hello, my name is {:10}. Nice to meet you !".format(name))
print("Hello, my name is {:>10}. Nice to meet you !".format(name))
print("Hello, my name is {:<10}. Nice to meet you !".format(name))
print("Hello, my name is {:^10}. Nice to meet you !".format(name))

print("===========================================================================")
#formatting some numbers
number = 3.14149

#using .2f means format the number to be a floating number with 2 digits on the right
print("The number pi is {:.2f}".format(number))
#keep in mind, the format method rounds the number
print("The number pi is {:.3f}".format(number))

second_number = 1000
#will add a comma to the numbers
print("The new number is {:,}".format(second_number))
#turn the number into binary
print("The new number is {:b}".format(second_number))
#turn the number into octal
print("The new number is {:o}".format(second_number))
#turn the number into hex
print("The new number is {:x}".format(second_number))
print("The new number is {:X}".format(second_number))
#turn the number into scientific notation
print("The new number is {:E}".format(second_number))