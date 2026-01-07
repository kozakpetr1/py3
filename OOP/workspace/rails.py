class RailFence:
    
    # počáteční inicializace vlastností objektu
    def __init__(self, rails = 3):
        self.__rails = rails    # počet kolejnic == 3
        self.__ot = ""          # otevřený text
        self.__ot_len = 0       # délka otevřeného textu
        self.__ct = ""          # šifrovaný text
        self.__ct_len = 0       # délka šifrovaného textu
         
    # šifruje open_text
    def encrypt(self, open_text):

        self.__ot = open_text                   # vlastnosti self.__ot přiřadíme hodnotu paramteru open_text
        self.__ot_len = len(self.__ot)   # vlastsnosti self.__ot_len přiřadíme délku řetězce selt.__ot
        self.__ct = ""
        
        row, asc = 0, True                      # row = aktuální řádek, col = aktuální sloupec, asc = True / False (vzestupně / sestupně)
        ct = [""] * self.__rails                # list s požadovaným počtem prázdných řetězců 
        
        for i in range(0, self.__ot_len):       # iterace otevřeného textu znak po znaku, zjišťujeme pozici řádku pro každý znak
            
            # tady je implementace šifrování            
            ct[row] += self.__ot[i]

            # zde určujeme číslo řádku pro každý znak otevřeného textu
            if (asc == True and row < self.__rails - 1):
                row += 1
            elif (asc == True and row == self.__rails - 1):
                asc = False
                row -= 1
            elif (asc == False and row > 0):
                row -= 1
            else:
                asc = True
                row += 1
        self.__ct = "".join(ct)
        return self.__ct
                      
    # dešifruje cypher_text
    def decrypt(self, cypher_text):
        pass
    
    # getter vrátí počet kolejnic
    def getRails(self):
        return self.__rails
    
    # getter vrátí otevřený text
    def getOpenText(self):
        return self.__ot
    
    # getter vrátí délku otevřeného textu
    def getOpenTextLen(self):
        return self.__ot_len

    # getter vrátí šifrovaný text
    def getCypherText(self):
        return self.__ct
    
    # getter vrátí délku šifrovaného textu
    def getCypherTextLen(self):
        return self.__ct_len

cypher = RailFence()
print(cypher.encrypt("ZVLADNOUTMATURITUJEDULEZITEALENEUSPECHJETAKEDULEZITAZIVOTNIZKUSENOST"))

cypher2 = RailFence(4)
print(cypher2.encrypt("ZVLADNOUTMATURITUJEDULEZITEALENEUSPECHJETAKEDULEZITAZIVOTNIZKUSENOST"))

