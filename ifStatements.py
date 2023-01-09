#if statement - block of code that willexecute if the condition is true

age = int(input("What is your age?: "))

""" if age >= 18:
    print("You are an adult")
elif age == 100:
    print("You are a century old")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are not an adult") """

#the order of the if statements matter
#elif age == 100 will not run because the first if statement is true

if age == 100:
    print("You are a century old")
elif age >= 18:
    print("You are an adult")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You are not an adult")

#logical Operators (and , or)
#used to check if two or more conditional statements are true or not

temp = int(input("What is the temperature outside?: "))
#both statements need to be true for the entire statement to be true
if temp >= 0 and temp <= 30:
    print("The temperature is nice!")
#only one statement needs to be true for the entire statement to be true
elif temp < 0 or temp > 30:
    print("It is scary to go outside!")

#using the not operator

temp2 = int(input("What is the temperature outside?: "))
#by placing the not() in between the two conditional statements, it reverses the conditional statement
#true will now be false, and false will now be true
if not(temp2 >= 0 and temp <= 30):
    print("It is scary to go outside!")
elif not(temp2 < 0 or temp2 > 30):
    print("The temperature is nice!")