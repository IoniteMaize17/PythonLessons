#'''
# loop through a string
for x in "banana":  # variable is declared here, rather than before the "for"
    print(x)

# loop through a list
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# use "break" to stop loop at 1 point before the end of list
for x in fruits:
    print(x)
    if x == "banana":
        break

# use "continue" to skip 1 point and continue the loop
for x in fruits:
    if x == "banana":
        continue
    print(x)

# using range(), sequence of numbers: range(start,end,step)
for x in range(7):  # range(7) mean x is int, from 0 to 7-1=6
    print(x)

for x in range(2, 8):  # still, range(2,8) mean the list is int and from 2 to 7, not 8
    print(x)

for x in range(10, 100, 10):
    print(x)

# when loop is finished, a block of code in "else" is executed
for x in range(1, 10):
    print(x)
    if x == 5:
        break
else:
    print("Ok, done. Going home!")
# cannot do this when look is break

# when loop is in loop, code run through inner loop for each instance of outer loop
for x in range(1, 3):
    for y in range(1, 3):
        print(x * y)
# this is also called multi-dimensional loop
