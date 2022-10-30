
def printer(stringstuff):
    stringrow = stringstuff
    print(stringrow)

#stringrow = "Defined in the main level."
#printer(stringrow)
#In here, the stringrow inside of function was given the value of the outside stringrow

def printer(stringstuff):
    stringrow = "Defined in the subfunction."
    print(stringrow)

#stringrow = "Defined in the main level."
#printer(stringrow)
#the variable stringrow is redefined in the function

def printer(stringstuff):
    stringrow = "Defined in the subfunction."
    print(stringrow)

#stringrow = "Defined in the main level."
#printer(stringrow)
#print(stringrow)
#the first printed stringrow is expected to be "in subfunction", not "in main level"
#but the second printed stringrow is surprisingly "in main level". 
# This is because the function did not have a return command, which would have affected the "main level" stringrow

#def print_price():
#   print(price)

#price = 100
#print_price()

def printlabel():
    if postbox == "30":
        print("P.O. Box 30")

postbox = "30"
printlabel()
