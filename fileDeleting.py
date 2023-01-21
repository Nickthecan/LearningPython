""" Before looking at "file" notes, you cannot run these files because the file names on my computer are different for your computer
If you are going to test this out, try replacing the directory names and file names with directories and files on your computer """

#deleting files
import os
import shutil

path = "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test4.txt"
#os.remove(path)

#but what happens if we try to delete a file that doesn't exist
#we will need to use the try statement

path2 = "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test5.txt"
try:
    os.remove(path2)
except FileNotFoundError:
    print("That file was not found !")

#the remove method does not remove empty folders
path3 = "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\emptyFolder"
try:
    #os.remove(path3) #deletes a file
    #os.rmdir(path3) #deletes an empty directory
    shutil.rmtree(path3) #this method is dangerous because this will delete a folder and everything within it
except FileNotFoundError:
    print("That file was not found !")
except PermissionError:
    print("You do not have permission to delete this folder !")
except OSError:
    print("You cannot delete that using that function'")
else:
    print(path3 + "was deleted")