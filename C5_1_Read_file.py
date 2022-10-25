


#file = open("demo.txt","a")
#file.write("Say hello")

from cgitb import handler


read_file= open("demofile.txt","r")
content = read_file.readlines()
print(content)
for i in content:
    print(i)
read_file.close()
'''
def readfile(name):
    try:
        readfile = open(name, 'r')
        content = readfile.read()
        readfile.close()
        return content
    except IOError:
        return False

readfile("demo.txt")
'''