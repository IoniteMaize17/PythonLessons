#reminder
#open("demo.txt","w") is to Write a new one and overwrite the old one
#open("demo.txt","a") is to Append, to write right after the end of the old one
#this is to ensure no IOError(means Input/Output error) happen, 
#which means the directory mentioned in code do not exist

demowrite = open("demofile.txt","w")

"""demotext = "\nFirst line!\nSecond line!\nThird line!"
print(demotext)

demowrite.write(demotext)"""
demowrite.write("")
demowrite.close()

# The first line in most coding examples is "# -*- coding: cp1252 -*-". 
# This means the code applies code page 1252, 
# Windows OS means the extended ASCII-chart for Western and Northern Europe.
# We can also do "# -*- coding: UTF8-*- ". The code page UTF8 has a lot of alphabets.
# Windows XP can be a bit problematic with this by newers OS works well.