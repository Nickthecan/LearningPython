# modules = a file containing python code. May contain functions, classes, etc
# used with modular programming, which is to separate a program into parts

#3 ways to import modules
#standard way
import messages
#giving an alias to the module
import messages as msg
#another way so you won't have to type message. or msg.
from messages import hello, bye
#importing all the functions (not recommended since you might run into naming conflicts if the modules are big)
from messages import *

#message.hello()
#message.bye()

#msg.hello()
#msg.bye()

hello()
bye()

#this might be tedious because you have to write more stuff in order to perform the function
#so we can give the module an alias (nickname)

#imported python modules
help("modules")