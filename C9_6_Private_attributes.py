class Score:
    __points = 0
    def results(self):
        return self.__points
#start the variable inside the class with "__" make it a private variable
#Meaning, it cannot be changed except by function from the same class
#Also the name cannot have more than one underscore(_) after the name
Red=Score()
Red.__points = 1
#print(Red.points)
print(Red.results())
#_[classname]__[variablename]