# print("Alo alo testing!")
# Global variable can be read and write by main level and function
# Meaning we can give it a value in a function without saying "return", and it is that value
# Declare a global variable this way:
#   commonvariable = ""
#   global  commonvariable
def printlabels():
    global postnumber
    if postnumber == "00102":
        print("Parliament house: 00102")
    postnumber = "99999"


"""
postnumber = "00102"
printlabels()
if postnumber == "99999":
    print("North Pole:",postnumber)"""

# The problem is when one function rewrites and another function reads that new rewrite.
# The old value is still needed while the new one needs to be remembered
