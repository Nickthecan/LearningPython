# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

""" def add(num1, num2):
    sum = num1 + num2
    return sum

print(add(1, 2, 3)) """
#this will not work since 3 numbers were passed into the add function which only has 2 arguments

#using *args will store all the arguments into a tuple 
def add(*args): #args is just a name and you can use any other name to it. The '*' symbol is the only thing that matters
    sum = 0
    #we can then iterate through the tuple and then add to the sum
    for i in args:
        sum += i
    return sum

#now, you can pass many numbers as you want
print(add(1, 2, 3))

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print("---------------------------")

def multiply(*stuff):
    sum = 0
    #stuff[0] = 0           You cannot edit a value in the tuple like this
    #you would need to typecast the tuple into a list
    stuff = list(stuff)
    #and then edit it
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(multiply(1, 2, 3))