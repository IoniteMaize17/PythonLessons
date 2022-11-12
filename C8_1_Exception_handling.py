#There are errors
#There is no way to prepare for them in a practical and meaningful manner
#We can try to fix all errors and prevent possible problems
#Python can highlight symptom and cause
#Here is a way. Try-except

mynumber = input("Give me number: ")

try:
    mynumber = int(mynumber)
    print("Got it,",mynumber)
except Exception:
    print("Hey, that is not a number!")
#inside the handler is the vulnerable code
#Typical vulnerable code are file opening, division with user input,
#dynamic structure,...