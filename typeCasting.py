#type casting = convert the data type of a value to another data type

#int
x = 1
#float
y = 2.0
#string
z = "3"
print("------------")
print(x)
print(y)
print(z)
print("------------")
print(x)
print(int(y)) #type casting y into an integer
print(z)
print("------------")
print(x + int(z)) #type casting z into an integer to do math

#concatenates a string with an int using type casting around the variable
print("X is " + str(x))