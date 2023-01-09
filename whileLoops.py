#while loop = a statement that will execute its block of code as long as its condition remains true

#if the while loop does not have an escape code, then the loop becomes an infinite loop
""" while 1 == 1:
    print("I am stuck in an infinite loop") """

name = ""

#using a while loop to continuously ask a user to enter their name if they don't enter anything
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)