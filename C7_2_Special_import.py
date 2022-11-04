'''def exit ():
    print("AAAA")
exit()'''
from sys import exit
'''def exit (a):
    print("AAAA")
exit(1)
exit("WHEN I WAS")'''

#As you can see, we imported function "exit" from module "sys".
#This imports only needed function, helps a lot with memory because not the whole module is imported
#Dont need to write sys.exit because now the exit is known
#Defining another exit after the import will overwrite the exit from sys.

from math import *
#Do this when absolutely sure about no conflict name