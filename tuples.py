#tuple = collection which is ordered and unchangeable used to group together related data

student = ("Nick", 19, "male")

#useful methods in a tuple
#----------------------------------------
#Return number of occurrences of value.
print(student.count("Nick"))
#Return first index of value.
print(student.index("male"))

#iterate throughout all the elements in the tuple
for x in student:
    print(x)
#conditional statement to see if an element is in the tuple
if "Nick" in student:
    print("Nick is here!")

#tuples are similar to lists however, they are unchangable