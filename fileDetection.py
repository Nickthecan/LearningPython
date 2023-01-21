""" Before looking at "file" notes, you cannot run these files because the file names on my computer are different for your computer
If you are going to test this out, try replacing the directory names and file names with directories and files on your computer """

#in order to manage files
import os

#checking to see if a file exists on the computer
#if your computer has '\' symbol, you will need to change it to '\\' since '\' is the escape sequence (\t, \n, etc)
path = "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test.txt"
path2 = "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python"

if os.path.exists(path):
    print("The location exists !")
else:
    print("That location doesn't exist !")
#however this doesn't tell you if it's a file

print("-------------------------------------")
#checks to see if the location is a file
if os.path.exists(path):
    print("The location exists !")
    if os.path.isfile(path):
        print("The location is also a file !")
else:
    print("That location doesn't exist !")

print("-------------------------------------")
#checks to see if the location is a directory
if os.path.exists(path2):
    print("The location exists !")
    if os.path.isfile(path2):
        print("The location is also a file !")
    elif os.path.isdir(path2):
        print("The location is also a directory !")
else:
    print("That location doesn't exist !")