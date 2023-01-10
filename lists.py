# list = used to store multiple items in a single variable

#creating a list requires a set of brackets []
food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

#overwrites the previous element at index 0
food[0] = "sushi"
#append function allows you to add an element to a list
food.append("ice cream")
#remove function allows you to remove an element from a list
food.remove("hotdog")
#pop function allows to remove the last element from a list
food.pop()
#insert function allows to insert an element into a position
food.insert(1, "cake")

#print out the list (should have added ice cream, removed hotdog, removed ice cream, and inserted cake into the first index)
for x in food:
    print(x)
print("-------------------")

#sort rearranges the list alphabetically
food.sort()

#print out the list (should be listed alphabetically)
for x in food:
    print(x)
print("-------------------")

#clear function clears the list
food.clear()

#print out the list (should be empty since we cleared it)
for x in food:
    print(x)


#================================================================================================================================

#2D lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]
#storing the lists in a bigger list (2D list)
food = [drinks, dinner, dessert]

print(food)
#prints the third item in list 1 (tea in drinks)
print(food[0][2])
#prints the second item in list 2 (hamburger in dinner)
print(food[1][1])
#prints the first item in list 3 (cake in dessert)
print(food[2][0])