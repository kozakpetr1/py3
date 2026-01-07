class Zvire:
    
    pocet_zvirat = 0
    
    def __init__(self, vaha, pohlavi, vyska):
        self.__vaha = vaha
        self.__pohlavi = pohlavi
        self.__vyska = vyska
        Zvire.pocet_zvirat += 1

    def __str__(self):
        return str(self.__vaha) + ", " + self.__pohlavi + ", " + str(self.__vyska)
    
    def __del__(self):
        print("Obecné žvíře bylo eliminováno.")
        Zvire.pocet_zvirat -= 1
            
class Savec(Zvire):
    
    def __init__(self, vaha, pohlavi, vyska, delka_tehotenstvi):
        Zvire.__init__(self, vaha, pohlavi, vyska)
        self.__delka_tehotenstvi = delka_tehotenstvi

    def __str__(self):
        return super().__str__() + ", " + str(self.__delka_tehotenstvi)

    def __del__(self):
        print("Savec byl eliminován.")
        Zvire.pocet_zvirat -= 1

print(Zvire.pocet_zvirat)
obecne_zvire = Zvire(20,"F", 35)
print(Zvire.pocet_zvirat)
obecny_savec = Savec(60, "M", 165, 9)
print(Zvire.pocet_zvirat)
del obecne_zvire
print(Zvire.pocet_zvirat)

