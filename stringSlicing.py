#slicing = create a substring by extracting elements from another string
#          indexing[] or slice()
#          [start: stop: step]

name = "Nicholas Amancio"
#start is inclusive, end is exclusive
firstName = name[0:8]
lastName = name[9:16]
funkyName = name[0:8:2]
reversedName = name[::-1]

print(firstName)
print(lastName)
print(funkyName)
print(reversedName)

#you can also write the index like this since python interprets the start or end point
shortcut1 = name[:8]
shortcut2 = name[9:]
shortcut3 = name[::2]

print("-------------------------------")

website = "http://google.com"
website2 = "http://wikipedia.com"
#slice function is a bit different
#find the starting point and end point and use commas to separate them
slice = slice(7, -4) #-4 is used to count backwards since if we want to use multiple website names, they are of different lengths

print(website[slice])
print(website2[slice])