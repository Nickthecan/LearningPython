#index operator [] = gives access to a sequence's elements (str, lists, tuples)

name = "nicholas amancio"
#if the name at index 0 is lowercase, print out true
if (name[0].islower):
    print("The letter is lowercase.")
#if not, print out false
else:
    print("The letter is not lowercase.")
print("-----------------------")

#you can use the index operator in order to create a new String from an existing string using [starting:ending]
first_name = name[0:8].upper() #upper for no reason
#[:8] is a shortcut
#[9:] is also a shortcut
print(first_name)

last_name = name[9:].lower()
print(last_name)

#you can use negative numbers to count backwards 
last_character = name[-1]
print(last_character)


