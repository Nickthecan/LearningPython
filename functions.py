#function = a block of code which is executed only when it is called

def hello():
    print("Hello!")

hello()
hello()
hello()
print("---------------------")

#functions can have more than one statement

def hellooo():
    print("Hello!")
    print("Have a nice day!")

hellooo()
print("---------------------")

#you can send information to the function to do something with the information
def hola(name): #this is an argument
    print("hello " + name)

hola("Nick")
print("---------------------")

#you can use multiple arguments in a function
def holaaaa(first_name, last_name):
    print("Hello " + first_name + " " + last_name)

name1 = "Nicholas"
name2 = "Amancio"

#the argument and the variable name do not have to match. The argument name is like a nickname used inside the function
holaaaa(name1, name2)
print("---------------------")

#=============================================================================================================================
#return statements = Functions send Python value/objects back to the caller
#                    These values/objects are known as the function's return value

def multiply(number1,number2):
    result = number1*number2
    return result

multiply(6, 8)
#however, this will not show up to the caller so there are a few ways to show the output
#you can use a print statement
print(multiply(6, 8))

#use a variable
x = multiply(6, 8)
print(x)
print("---------------------")

#=============================================================================================================================
#keyword arguments = arguments preceded by an identifier when we pass them into a function
#                    The order of the arguments doesn't matter, unlike positional arguments
#                    Python knows the names of the arguments that our function receives

def hi(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hi("Amancio", "Nicholas", "Jacob")
#the function will print the names out of order since there isn't any keyword arguments
#Hello Amancio Nicholas Jacob 

hi(last = "Amancio", first = "Nicholas", middle = "Jacob")
#now the function will print everything in order since the keyword arguments are listed
print("---------------------")

#=============================================================================================================================
#nested functions calls = function calls inside other function calls
#                         innermost function calls are resolved first
#                         returned value is used as the argument for the next outer function

#using multiple methods in order to take in a number
num = input("Enter a whole positive number: ")
#turn it into a float
num = float(num)
#take the absolute value
num = abs(num)
#round it to the nearest number
num = round(num)
#and then print the new number
print(num)

#using nested functions
print(round(abs(float(input("Enter a whole positive number: ")))))
#this does the same as the previous code but it is all shortened down
