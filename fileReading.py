""" Before looking at "file" notes, you cannot run these files because the file names on my computer are different for your computer
If you are going to test this out, try replacing the directory names and file names with directories and files on your computer """

#in order to read a file
with open("C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test.txt") as file:
    print(file.read())
#this will close the file automatically after opening them

#lets test this (True = closed, False = open)
print(file.closed)
print("------------------------------------------------")

#however this means that if a file is incorrectly inputted, the file will stay open
#use a try statement
try:
    with open("C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test.tx") as file:
        print(file.read())
except FileNotFoundError:
    print("File was not found")
