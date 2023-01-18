#scope = the region that a variable is recognized
#        a variable is only available from inside the region it is created
#        a global and locally scoped versions of a variable can be created

name = "Anna" #global variable (available outside and inside functions)

def display_name():
    name = "xie" #local scope (only available inside the function)
    print(name)

#the name will change due to the local variable being updated inside the function
display_name()
#however the name stays the same since it is a global variable
print(name)
#if line 5 was never written, line 14 would never work since the variable name is not defined at all, only inside the function

#Python uses a variable rule called LEGB
#L = Local
#E = Enclosing
#G = Global
#B = Built-in