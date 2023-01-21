#exceptions = events detected during execution that interrupts the flow of a program

def divide():
    num = int(input("Enter a numerator: "))
    den = int(input("Enter a denominator: "))
    result = num / den
    return result

#print(divide())

#what happens if we divide by zero

""" Traceback (most recent call last):
  File "fileName", line 9, in <module>
    print(divide())
  File "fileName", line 6, in divide
    result = num / den
ZeroDivisionError: division by zero """

#use a try statement to test dangerous code

try:
    num = int(input("Enter a numerator: "))
    den = int(input("Enter a denominator: "))
    result = num / den
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by 0 !")
except ValueError as e:
    print(e)
    print("Enter only numbers.")
except Exception:
    print("Something went wrong...")
#when there are no more exceptions left
else:
    print(result)
#this is always at the end. Even if we catch an exception, we will always run this block of code
#useful for closing files when dealing with files
finally:
    print("This will always execute")

#now the try will catch the exception and continue running the code without being interrupted
#you can catch multiple exceptions
#don't just use "Exceptions" because it is considered bad practice
