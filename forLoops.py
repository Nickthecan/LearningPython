#time module, used for waiting (countdown)
import time

#for loop = a statement that will execute its block of code for a limited amount of times
#
#           while loop = unlimited times
#           for loop = limited times

#range = execute for n amount of times. In this case, we're looping through the block of code 10 times
for i in range(10):
    print(i + 1)

#everytime it loops through the block, the index (i) will increase by 1
#thats how the loop know when to stop because when the index hits 10, it will jump outside the block of code

#range function from 50 to 100, first number is inclusive and second number is exclusive
for i in range(50, 100):
    print(i)

#third parameter will be the step number. you can choose how much to increment i by everytime the loop runs through the block of code
for i in range(50, 100, 2):
    print(i)

#You can use a string and using a for loop, you can iterate through all the letters in your name
for i in "Nicholas Amancio":
    print(i)


#code for a countdown
#---------------------------------------------------------------
#range : from 10 to 0 with a step of -1 (decrementing)
for seconds in range(10, 0, -1):
    print(seconds)
    #wait 1 second
    time.sleep(1)
#make sure the print statement is outside the for loop
print("Happy New Year!!!")