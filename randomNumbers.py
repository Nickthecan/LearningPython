#import module that creates random numbers
import random

#rolling a dice
#using the randint method and the range from 1 - 6, we can simulate a dice roll
x = random.randint(1,6)
#print a floating point number
y = random.random()

print(x)
print(y)

#choice method to get a random item from a list
myList = ["rock", "paper", "scissor"] 
z = random.choice(myList)

print(z)

#shuffle method to rearrange the list 
cards =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)