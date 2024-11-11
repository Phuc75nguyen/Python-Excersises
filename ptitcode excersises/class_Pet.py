class Pet:
    def __init__(self, newAgePet, newName, newVoice, newFood):
        self.__agePet = newAgePet
        self._name = newName
        self._voice = newVoice
        self.__food = newFood
    
    def getAge(self):
        return self.__agePet
    
    def getName(self):
        return self._name
    
    def getVoice(self):
        return self._voice
    
    def getFood(self):
        return self.__food

    def __str__(self):
        return f"Pet's Name: {self._name}\nAge: {self.__agePet}\nVoice: {self._voice}\nFavorite Food: {self.__food}"


pet1 = Pet(21, "Chimcook", "Quatquat", "Hamburger")


print(pet1)
