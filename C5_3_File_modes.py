number = 1024

readfile = open("numberfile.txt","w")
#the "w" do this: if file name matches no file, creates new file.
#if it does, empties the file before writing. Handles data as characters
readfile.write( str(number) )
#This writes the "number" as string
readfile.close()

readnumber = 0
readfile = open("numberfile.txt","r")
readnumber = int(readfile.readline())
readfile.close()
print("A number",readnumber," was read and converted to a number:")
readnumber = readnumber *2
print(readnumber)