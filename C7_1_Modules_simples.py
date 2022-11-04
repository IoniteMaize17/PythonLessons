#There are functions that are already created to help with trivial matters. 
#For example, using a network connection or implementing a clock in the program.
#These functions are not known by the program until they are called in groups.
#Groups of functions are called library or modules.
#Python has a lot of modules that help with many different problems: math, randoming, GUI building, using Internet connection, using audio files.
#We start to work with module by this:
#import random
#this tell the interpreter that I am going to work with a bunch of functions in the module function
#this module helps with picking random numbers or elements
#for example

#Of course, like any other number range in Python we learned so far, this function is picking from 0 to 99, so 100 is left alone

#print("Program picked a number", random.randint(0,100))
'''def randint( a,  b):
    print("This function does not do a thing.")
randint(1,2)'''
#import math
#print(dir(math))
#print(math.__name__)
#print(math.__doc__)
#print(math.__loader__)
#print(math.__package__)
#print(math.__spec__)
#import tkinter
#help(tkinter)
#help(math)
#help(random)
import sys
price = int(input("JUST GIVE ME REEEASON: "))
if price > 0:
    print("I'm OUT.")
    sys.exit("L0l") #Yep, this is the exit notification
else:
    tax = int(input("FOR ALL IVE DONE: "))
if tax > 0:
    print("I'm still out.")
    sys.exit(0)
else:
    print("NANANANANANA")
#exit() command is helpful. Doesnt need to be bypassable. Example, GUI needed a clean exit, not a loop with break command.
#exit parameter is a notification about why the exit was done
#in the example, normally the second "if" should be inside the else. But with the help of sys.exit, it does not.
