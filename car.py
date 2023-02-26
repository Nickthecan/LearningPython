#Use classes to assign attributes to the object
class Car:
    #each car (Object) will be assigned the same class variable
    wheels = 4   #class variables

    #Create a constructor in order to construct the object for us
    def __init__(self, make, model, year, color):
        #self will be passed into the other methods
        #self is the same as this. method in Java
        self.make = make    #instance variables
        self.model = model  #instance variables
        self.year = year    #instance variables
        self.color = color  #instance variables

    #created methods for the car object
    #with self, it uses the constructor's arguments so we do not have to pass any arguments into the methods with the parameter of "Self"
    def drive(self):
        print("This {} is driving".format(self.model))

    def stop(self):
        print("The {} has stopped".format(self.model))

#The nice thing about Objects is that it is a blue print so we can create multiple car objects and assign different arguments to it
#Another example for creating Objects is like creating a user profile on a website. A user profile requires a username and a password.
#It would be annoying to create multiple Objects by instantiating with multiple variables

#user1_username = "Name"
#user1_password = "password"
#user2_username = "Name"
#user2_password = "password"
#user3_username = "Name"
#user3_password = "password"

#we can use Objects so it can be a lot easier

#user1("Name", "Password")
#user2("Name", "Password")
#user3("Name", "Password")

#Class Variables vs. Instance Variables
#Class Variables are instantianted outside the constructor while the Instance Variable is instantiated inside the constructor. The Class Variable is 
#assigned to all objects while the Instance Variable is assigned to a particular object.