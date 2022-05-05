class DCComics:
    def __init__(self, **kwargs):
        self.__name = str(kwargs["name"]) if "name" in kwargs.keys() else ""
        self.__born = int(kwargs["born"]) if "born" in kwargs.keys() else 0
        self.__bestActorName = str(kwargs["aname"]) if "aname" in kwargs.keys() else ""
        self.__weapons = list(kwargs["weapons"]) if "weapons" in kwargs.keys() else []
        
    def __str__(self):
        return "DCComics: {}, {}, {}, {}".format(self.__name, self.__born, self.__bestActorName, self.__weapons)

SuperMan = DCComics(name="Superman", born=1938, aname="Henry Cavill", weapons=["power"]) 
print(SuperMan)
BatMan = DCComics(name="Batman", weapons=["richness", "flying"])
print(BatMan)
Unknown = DCComics()
print(Unknown)