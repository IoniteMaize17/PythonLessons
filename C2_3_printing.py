print("I'm printing stuffs!")
variable = 4
print("I'm printing",variable,"stuffs!",end="lol")
score = "F"
print("I got an",score+"!")
print("I got an",end=score+"!")
text = "This text has a line change. \n"
print(text)
print(repr(text))
number1 = 1.1
number2 = 1.5555
print(round(number1),round(number2,2))
if True:
    print("This is a very big, long \
and even annoying command which takes way too \
much space and is irritating to handle") #The continue slash tech can be done with the second line start at the start of the line
#identation is ignored

#Predefined string
print(""" There are several things
- potatoes
- cauliflowers""") #A """ or a ''' means that everything comes after is in the same string, including 
# line breaks, indentation, etc until another triple quotation 

print("Do we see \
'\\' this or what? What does this \ do?")
#the \ also let interpreter disregard the next layout-affecting modifier, or to bypass the next quotation mark and continue the string

print("fwefw\"fwfqfqfewqf")
print('khfwa\'j')

#citation and quotation marks are interchangeable, allow the use of one or another on a string

print("ah'a")
print('ah"a')

#However, stick to 1 mark and use \ is better, more consistent

print("He screamed:\"You shall not pass\"")

#Layouts characters like \n, \f are each counted as 1 character. There can be as many as possible
print("\n\n\nLine breaks!\n\n")

#Some combinations of layout character can make printouts 
print("\t1\t2\n\t3\t4")