#set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}

#prints out all the elements in the set
print("utensils set")
print("----------------------------")
for x in utensils:
    print(x)
print()
#There is a difference in printing the elements since they aren't indexed. This means the order they come in are random
#For time complexity, a set is actually faster than a list if you need to check to see if an element is within a set compared to a list

utensils2 = {"fork", "spoon", "knife", "knife", "knife", "knife"}

print("utensils2 set")
print("----------------------------")
for x in utensils2:
    print(x)
print()
#Since the set does not contain duplicates, it will ignore the duplicates if a user adds them in.

#useful methods in a set
#--------------------------
#add an element to the set
utensils.add("napkin")
#remove an element from the set
utensils.remove("fork")
#clear the set
utensils.clear()

#lets add another set
dishes = {"bowl", "plate", "cup", "knife"}

#updates the utensils2 set with the elements in dishes set
utensils2.update(dishes)
#print the updated set
print("utensils2 set with the added elements of dishes")
print("----------------------------")
for x in utensils2:
    print(x)
print()

utensils3 = {"fork", "spoon", "knife"}
#add a new set with a combination of both utensils3 and dishes
dinner_table = utensils3.union(dishes)
print("dinner_table set with the union of utensils3 and dishes")
print("----------------------------")
for x in dinner_table:
    print(x)
print()
#add a new set with the shared elements from utensils3 and dishes
dinner_table2 = utensils3.intersection(dishes)
print("dinner_table set with the intersection of utensils3 and dishes")
print("----------------------------")
for x in dinner_table2:
    print(x)
print()
#adds a new set with what do utensils3 has that dishes do not
dinner_table3 = utensils3.difference(dishes)
print("dinner_table set with the difference of utensils3 and dishes")
print("----------------------------")
for x in dinner_table3:
    print(x)
print()