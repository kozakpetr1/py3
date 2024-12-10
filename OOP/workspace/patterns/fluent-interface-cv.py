class Jidlo:
    
    def __init__(self):
        self.__co = ""
        self.__i = []
        
    def coVarit(self, nazev):
        self.__co = nazev 
        return self
    
    def pridatIngredienci(self, ingredience):
        print("Přidal jsem ingredienci:", ingredience)
        self.__i.append(ingredience)
        return self

    def zamichat(self):
        print("Zamíchal jsem ingredience:", self.__i)
        return self

    def uvarit(self, teplota, cas):
        print(f"Vařil jsem {cas} minut na {teplota} stupňů.")
        return self
        
    def upect(self, teplota, cas):
        print(f"Pekl jsem {cas} minut na {teplota} stupňů.")
        return self

    def servirovat(self, ):
        print(f"Naservíroval jsem Vám {self.__co} obsahující tyto ingradience: {self.__i}")
        return self

j = Jidlo()
j.coVarit("Ovocný čaj").pridatIngredienci("Ovocný čaj Teekanee").pridatIngredienci("voda").uvarit(100, 1).zamichat().servirovat()