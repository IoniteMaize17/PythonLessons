#infinite loop is when the number of turns is not determined.
#Programmers keep the loop running until a condition is met

#these codes go along with the input. It is not automated until a point is reached
#'''
keepgoing = True

while keepgoing:
    userwrote = input("Write something: ")

    if userwrote == "End":
        keepgoing = False
    else:
        print(userwrote)

#Automated process needs a "break"

startpoint = int(input("Give the starting point: "))

while True: # the "while True" loop will run till "break"
    if startpoint % 10 == 0:
        print(startpoint)
        print("VIVONZULUL!")
        break
    else:
        print("Currently we are at", startpoint)
        startpoint += 1