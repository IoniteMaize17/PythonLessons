#string slicing
bigstring = "auxiliaryemergencyfirepreventionsystem"
bigstring2 = ""
print(len(bigstring))
print(bigstring[len(bigstring)-1])
print([bigstring][0]) #this makes the string 1 element, meaning cannot count other than 0 and -1

#slicing several characters
print(bigstring[-3:40:2])#if end point exceed the last position, auto-adjust the end poin to last position
print(bigstring[-3:-5:2])#if start point exceed end point, return empty string (not error)
print(bigstring[-3:-7:-2])#to moon_walk(), use negative step
print(bigstring[::-1])#this use the default value of start point and end point (can show the end point)
print(len(bigstring2))