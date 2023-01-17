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