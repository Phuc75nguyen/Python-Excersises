class Person():
    __name = "" #private
    _age = 0
    
    def __init__(self, newName, newAge):
        self.__name = newName
        self._age = newAge
        
        
        
    def showAge(self):
        print("%s age %d" % (self.__name, self._age))
        
    def getAge(self):
        return self._age
    
    def setAge(self):
        return self._age
    
person1 = Person("Phuc", 21)
person1.showAge()

print(person1.getAge())


                