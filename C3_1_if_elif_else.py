color = input("What is your favorite color?: ").casefold()

#Let's define the selection argument and see if it was "blue"
#Notice the new indentation level inside the structure
if color == "Blue".casefold():
  print("Blue is nice.")

else:
  print(color.capitalize(), "is also nice.")
print("This line follows the if-structure and is always executed.")

#other than the if, the program does not react. We can add some reactions for other inputs
#bLuE, blUE,BLuE,.... To be case-insensitive, use casefold() on both input and condition
#bad to use an editor to edit Python source code because they cannot handle indentation well
#indentation should always be used with the space bar, not tabulator.
#however, good editor that understand python is usable
#after if is else

#short hand if
if color == "Red".casefold(): print("Good! Warm color.")

#short hand if-else
print("Good Green") if color == "Green" else print("A bit green is good.")

#if not (value_2 == "Run Away!"):
#      print("Its alive!")


if True:
  print("a")

if (not (1 == 1)):
  print("b")

if False:
  print("c")
elif False:
  print("d")
elif True:
  print("e") #the if-elif-else structure resolve by going straight down and stopping at first true place. Others are ignored, even if they are true
elif False:
  print("f")
else:
  print("g") #it is a good habit to have an else in every if-else sequence. It is easier to check for mistakes if there is a closing line.


