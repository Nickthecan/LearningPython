""" Before looking at "file" notes, you cannot run these files because the file names on my computer are different for your computer
If you are going to test this out, try replacing the directory names and file names with directories and files on your computer """

#moving files
import os

#variable that contains our source (from my python folder)
source = "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test3.txt"
#variable that contains our destination (to my desktop)
destination = "C:\\Users\\AwesomePiggy44\\Desktop\\test3.txt"

try:
    #in case you don't want to overwrite any files
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")

#you can use this to move directories by renaming the source and destination variables
