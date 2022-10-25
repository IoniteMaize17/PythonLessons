# Lets make a new fuction
def hellofunction():
    print("This print is from the function!")


# hellofunction()


def Comparison(number_1, number_2):
    if number_1 == number_2:
        print("The numbers are equal.")
    elif number_1 > number_2:
        print("The first number is larger.")
    else:
        print("The second number is larger.")


# help()


def my_function(*kids):
    # this makes the variable a list. Looks normal like a print function
    print("The youngest child is " + kids[2])


# my_function("Emil","Tobias","Linus")


def my_function_2(child3, child2, child1):
    # Assign keywords to variables so that the order of them does not matter
    print("The youngest child is " + child3)


# my_function_2(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# a, b = 0, 1


def change_price(value):
    value = 250 + value


# This function looks ok but it actually give you a None if you try
# printing the result. Also after you call the function, you can check the "value"
# and see it did not change. This means the function was not told to give us anything
value = 100
price = change_price(value)
# print(price)
# change_price(value)
# print(value)


def actual_change_price(value):
    value = 250 + value
    return value
    # x = 1


price = actual_change_price(value)
# print(price)
# now with the return command, the function works perfectly
# the return command can work with object (variables, functions, etc...)
# the function ends immediately if it encounters return value.
# it is good idea to make several return value to avoid errors
