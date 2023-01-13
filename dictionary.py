#Dictionary = A changeable, unordered collection of unique key: value pairs
#             Fast because they use hashing, allow us to access a value quickly

capitals = {"USA": "Washington DC", "India": "New Dehli", "China": "Beijing", "Russia": "Moscow"}

#instead of using an index, you reference the key to get its value
print(capitals["Russia"])
print("----------------------")
#this will print out Moscow

#however this is not a good way to display a value
#print(capitals["Germany"])
#this will give an error since Germany is not in the "capitals" Dictionary

#use the get method to safely retrieve a key
print(capitals.get("Germany"))
#method to print only keys
print(capitals.keys())
#method to print only values
print(capitals.values())
#method to print everything
print(capitals.items())
print("----------------------")

#printing out the items in capitals using a for loop
for key,value in capitals.items():
    print(key, value)
print("----------------------")
#updating the dictionary
capitals.update({"Germany": "Berlin"})

for key,value in capitals.items():
    print(key, value)
print("----------------------")
#rewriting a key value
capitals.update({"USA": "Las Vegas"})

for key,value in capitals.items():
    print(key, value)
print("----------------------")
#pop method to remove a key value pair
capitals.pop("China")

for key,value in capitals.items():
    print(key, value)
print("----------------------")
#clear method to clear the dictionary
capitals.clear()
print(capitals.items())
