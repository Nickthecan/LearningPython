
#assign the input into the variable "name"
name = input("What is your name?: ")
print("Hello " + name)

#input function only takes in string data types
#need to cast it 
age = int(input("How old are you?: "))
age += 1

#you would need to bring it back to a string data type in order to concat
print("Your age is " + str(age))

height = float(input("How tall are you?: "))
print("you are " + str(height) + " cm tall")