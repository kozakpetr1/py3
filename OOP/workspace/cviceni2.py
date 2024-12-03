class Zak:
    
    def __init__(self):
        self.__jmeno = ""
        self.__prijmeni = ""
        self.__trida = ""
        self.__inf = ""
        
    def setJ(self, jmeno):
        self.__jmeno = jmeno
        self.__inf = jmeno
        return self

    def setP(self, prijmeni):
        self.__prijmeni = prijmeni
        self.__inf += " " + self.__prijmeni
        return self
        
    def setT(self, trida):
        self.__trida = trida
        self.__inf += " je žákem třídy " + self.__trida + "."
        return self
    
    def getInfo(self):
        return self.__inf
        
z = Zak()
z.setJ("Jan").setP("z Vysočan").setT("2ITE")
print(z.getInfo())
