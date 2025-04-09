class VystiraciKad:
    
    def vystirani(self):
        return "Smíchání namletého sladu s teplou vodou za vzniku kašovité směsi."

class RmutovaciKotel:
    
    def rmutovani(self):
        return "Postupné zahřívání směsi na různé teploty pro přeměnu škrobů na cukry."

class ScezovaciKad:

    def scezovani(self):
        return "Oddělení tekuté sladiny od pevných zbytků sladu (mláta)."

class VarnyKotel:
    
    def vareniSladiny(self):
        return "Vaření sladiny s chmelem pro získání hořkosti a aroma."
        

class ChladiciZarizeni:
    
    def chlazeni(self):
        return "Rychlé zchlazení uvařené mladiny na teplotu vhodnou pro kvašení"
    
class Spilka:
    
    def hlavniKvaseni(self):
        return "Přidání kvasnic; přeměna cukrů na alkohol a oxid uhličitý."

class LezackySklep:
    
    def dokvasovani(self):
        return "Dozrávání piva, nasycení oxidem uhličitým, vyvážení chutí."

class Stacirna:
    
    def filtraceStaceni(self):
        return "Případná filtrace a plnění piva do lahví, sudů či plechovek."

class Pivovar:
    
    def __init__(self):
        self.__vystiraci_kad = VystiraciKad()
        self.__rmutovaci_kotel = RmutovaciKotel()
        self.__scezovaci_kad = ScezovaciKad()
        self.__varny_kotel = VarnyKotel()
        self.__chladici_zarizeni = ChladiciZarizeni()
        self.__spilka = Spilka()
        self.__lezacky_sklep = LezackySklep()
        self.__stacirna = Stacirna()
        
    def uvarPivo(self):
        pivo = [
            self.__vystiraci_kad.vystirani(),
            self.__rmutovaci_kotel.rmutovani(),
            self.__scezovaci_kad.scezovani(),
            self.__varny_kotel.vareniSladiny(),
            self.__chladici_zarizeni.chlazeni(),
            self.__spilka.hlavniKvaseni(),
            self.__lezacky_sklep.dokvasovani(),
            self.__stacirna.filtraceStaceni()
        ]
        separator = "\n"
        return separator.join(pivo)
        
pivovar = Pivovar()
print(pivovar.uvarPivo())
        