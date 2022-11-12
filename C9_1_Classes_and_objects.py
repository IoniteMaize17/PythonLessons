class new_class:
    x = 5

    def y(self):
        return "Hello world"
##### The class is a kind of prototype or schematic for an object, 
##### and defines the different methods and attributes the class — and the subsequent object — will have.

# print(new-class)
#object1 = new_class()
# print(object1)
#object2 = new_class.y("zzzz")
#print(object2)


class Person:
    def __init__(a, b, c, d, e):
        # init is short for initializing. This happen whenever a class is called first time.
        a.name = b
        a.age = c
        a.school = d
        a.rank = e


# Any number of slot can be taken. Well, almost, there is an upper limit.
# The first one will be the slot for an object that will be called later
# from the 2nd slot onwards, those are for attributes that will be called along with the new object

# __init__() is the function to assign stuff for objects

p1 = Person("John", 36, "Ams", "Comedian")
#now the object "p1" has a set of value as we design in the class "Person"
# print(p1.name)
# print(p1.age)
# print(p1.school)
# print(p1.rank)
# print(__main__.Person)
