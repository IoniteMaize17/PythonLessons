class Burger:
    buns = 2
    salad =1
    meat = 1
class Cheeseburger (Burger): #This is how to inherit class
    cheese = 1

#order1 = Cheeseburger()
#print(order1.cheese)

class Smoothies:
    fruit = "avocado"

class Smoothies_Cheeseburger(Cheeseburger,Smoothies):
    straw = True
#This is how to inherit multiple classes, should be avoided to avoid conflict.
order2 =Smoothies_Cheeseburger()
print(order2.straw)