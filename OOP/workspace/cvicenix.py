class Dog:
    
    count = 0
    
    def __init__(self, race, name, age, sex):
        
        self.__name = name
        self.__race = race
        self.__age = age
        self.__sex = sex
        Dog.count += 1
        
    def __del__(self):
        Dog.count -= 1
        
    def __str__(self):
        return self.__race + ", " + self.__name + ", " + str(self.__age) + self.__sex

    def getRace(self):
        return self.__race
    
    def setRace(self, race):
        self.__race = race
    
    
shiba_inu = Dog("Shiba Inu", "Guču", 1, "F")
print(shiba_inu)
print(shiba_inu.getRace())
shiba_inu.setRace("Shiba-Inu")
print(shiba_inu.getRace())
cau_cau = Dog("Čau Čau", "Hajzl", 2, "M")
print(cau_cau)
    
    