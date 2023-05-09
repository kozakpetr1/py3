class DCComics:
    def __init__(self, **kwargs):
        self.__name = str(kwargs["name"]) if "name" in kwargs.keys() else "Unknown"
        self.__born = int(kwargs["born"]) if "born" in kwargs.keys() else 0
        self.__bestActorName = str(kwargs["aname"]) if "aname" in kwargs.keys() else "Unknown"
        self.__weapons = list(kwargs["weapons"]) if "weapons" in kwargs.keys() else []
        
    def __str__(self):
        return "DCComics: {}, {}, {}, {}".format(self.__name, self.__born, self.__bestActorName, self.__weapons)
    
    def setName(self, name):
        self.__name = str(name)

    def setBorn(self, born):
        self.__born = int(born)

    def setBestActorName(self, aname):
        self.__bestActorName = str(aname)

    def getName(self, name):
        return self.__name

    def getBorn(self, born):
        return self.__born

    def getBestActorName(self, aname):
        return self.__aname
    
    def addWeapon(self, weapon):
        self.__weapons.append(weapon)
    
    def removeWeapon(self, weapon):
        self.__weapons.remove(weapon)
    
    def getWeapons(self):
        return self.__weapons

SuperMan = DCComics(name="Superman", born=1938, aname="Henry Cavill", weapons=["power"]) 
print(SuperMan)

BatMan = DCComics(name="Batman", weapons=["richness"])
print(BatMan)
BatMan.setBorn(born = 1939)
print(BatMan)
BatMan.setBestActorName(aname = "Ben Affleck")
print(BatMan)
BatMan.addWeapon(weapon = "flying")
print(BatMan)
BatMan.removeWeapon(weapon = "richness")
print(BatMan)

Unknown = DCComics()
print(Unknown)