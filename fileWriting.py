""" Before looking at "file" notes, you cannot run these files because the file names on my computer are different for your computer
If you are going to test this out, try replacing the directory names and file names with directories and files on your computer """

text = "\nASHHHFHWEUIRGHEAGREBKRYBEAKUYRBKERBKGUERB"

#writing a file
with open("C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test2.txt", 'w') as file:
    file.write(text)

#doing this will overwrite a file so in order to append stuff to a file, we use 'a'
with open("C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test.txt", 'a') as file:
    file.write(text)
