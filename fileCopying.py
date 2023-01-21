""" Before looking at "file" notes, you cannot run these files because the file names on my computer are different for your computer
If you are going to test this out, try replacing the directory names and file names with directories and files on your computer """

# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)

import shutil

#two arguments (source, destination)
shutil.copyfile("C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test2.txt",
                    "C:\\Users\\AwesomePiggy44\\Desktop\\Code\\Python Code\\Learning Python\\test3.txt")

#if you need to use the other methods, the arguments are exactly the same
#however, use the one that you need

#shutil.copy()
#shutil.copy2()