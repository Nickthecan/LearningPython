#a variable is a container for a value

#can automatically define a string, int, float, and booleans

#type function prints out the data type of the variable
name = "Nicholas Amancio"
print(type(name))

#can print out multiple variables of the same type
first_name = "Nicholas"
last_name = "Amancio"

print(first_name + " " + last_name)

#ints
age = 19
age += 1
print(age)
print(type(age))

#how to concatenate 
#typecasting is a way : converting the int variable into a string in order to print the same data type 
print("Your age is: " + str(age))

#multiple assignments to variables
Name, Age, Cute = "Anna", 18, True

SpongeBob = Patrick = Sandy = Squidward = 30