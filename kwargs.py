# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
#            short for "Key Word Arguments"

""" def hello(first, last):
    print("hello " + first + " " + last)

#what happens if the person has two names
hello(first = "Nicholas", middle = "Jacob", last = "Amancio") """

def hello(**kwargs): #don't have to name it kwargs, as long as the "**" symbol is there
    #print("hello " + kwargs["first"] + " " + kwargs["last"])
    print("Hello", end = " ")
    for key, value in kwargs.items():
        print(value, end = " ")


hello(title = "Mr.", first = "Nicholas", middle = "Jacob", last = "Amancio")