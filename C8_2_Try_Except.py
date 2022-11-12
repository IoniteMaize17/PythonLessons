def getnumber():
    number = input("Give a numeric value: ")
    return number

def main():
    number1 = getnumber()
    number2=getnumber()
    try:
        result =int(number1)/int(number2)
    except ZeroDivisionError: #One error class
        print("Its not possible to divide thiw 0.")
    except(TypeError, ValueError): #Two error classes
        print("Its not possible to calculate letters.")
    else: #all of others
        print("The result is",result)

main()
#if the except happen, the result in try will never be recorded.
#This leads to the function after the try-except have no value and will be errors