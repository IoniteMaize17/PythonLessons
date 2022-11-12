#try-except is to prevent crashing
#try-finally is to end the program on error, with some control
number = input("write here:")
try:
    number = int(number)
    print("Good,",number)
finally:
    print("Error! Error!")
#the "finally" part is to do something after the error
print("lol")
#while making fuction, it is good to define the user-give-number part separately
#and give it a try-except. Easy to fix things.
#Ctrl-C is to escape a running code page, 
# which raises the KeyBoardInterrupt error, 
# which by default is not caught by the Exception handler