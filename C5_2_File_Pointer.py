readfile = open("demofile.txt","r")



content = readfile.readline()
location = readfile.tell() #tell is
print(content[:-1] + "; The pointer is now at",location)
#The -1 for string "content" is to cut off the line breaks at the end 

#print("Return to character number 10:")
readfile.seek(0)
content = readfile.read()
print(content)
#The pointer is moved to position 10. 
#The command read now start reading from position 10

readfile.close() #always close data files

#variable readfile seems to be a pointer to do stuff to file demo.txt
#not the whole file demo.txt