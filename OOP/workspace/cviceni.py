from abc import ABC, abstractmethod

class Fluidum(ABC):
    
    @abstractmethod
    def stvoreni(self, **kwargs):
        pass
    
    @abstractmethod
    def potreba(self, **kwargs):
        pass
    
class Humunculus(Fluidum):
    
    def __init__(self):
        self.__jmeno = ""
        self.__pohlavi = ""
        self.__sila = 0

    def stvoreni(self, **kwargs):
        self.__jmeno = kwargs["jmeno"] if kwargs["jmeno"] else "Noname"
        self.__pohlavi = kwargs["pohlavi"] if kwargs["pohlavi"] else "Non binary"
        self.__sila = kwargs["sila"] if kwargs["sila"] else 1
        return self
        
    def potreba(self, ** kwargs):
        print(f"{self.__jmeno} provedl/a potřebu: {kwargs["jaka"]}")
        return self
        
    def __str__(self):
        return f"{self.__jmeno}, {self.__pohlavi}, {self.__sila}"
        
class Animal(Fluidum):
    
    def __init__(self):
        self.__nazev = ""
        self.__pohlavi = ""
        self.__strava = ""

    def stvoreni(self, **kwargs):
        self.__nazev = kwargs["nazev"] if kwargs["nazev"] else "Noname"
        self.__pohlavi = kwargs["pohlavi"] if kwargs["pohlavi"] else "Nonbinary"
        self.__strava = kwargs["strava"] if kwargs["strava"] else "všežravec"
        return self
        
    def potreba(self, ** kwargs):
        print(f"{self.__nazev} provedl/a potřebu: {kwargs["jaka"]}")
        return self

    def __str__(self):
        return f"{self.__nazev}, {self.__pohlavi}, {self.__strava}"
        
h = Humunculus()
h.stvoreni(jmeno = "Matěj Strnad", pohlavi = "Muž", sila = 999).potreba(jaka = "doplnění oleje")


a = Animal()
a.stvoreni(nazev = "Tygr", pohlavi = "Samec", strava = "masožravec").potreba(jaka = "podrbání se o strom")