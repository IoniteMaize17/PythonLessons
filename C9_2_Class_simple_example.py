class Switch:
    '''Switche-class, return a Boolean.'''
    __mode= False #the __ character is ok when use for naming
    def get_mode(self):
        return self.__mode
    def switch_mode(self):
        if self.__mode == False:
            self.__mode = True
        else:
            self.__mode = False
Lamp = Switch() 
#Lamp is now an object with Switch class, it can use methods/attributes in Switch
Lamp.get_mode()
Lamp.switch_mode()
#__mode is a private variable that cannot be changed outside of the class
#and can only be changed by using the class method
####
#Generally, class with attributes are like this
'''class [Name]:
    [attribute_1]=[default value]
    ...
    [attribute_N]=[default value]

'''