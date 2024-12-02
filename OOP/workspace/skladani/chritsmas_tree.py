class VanocniStrom:
    
    typ_stromku = ["borovice", "smrk", "jedle", "modřín", "umělý"]
    typ_ozdoby = ["koule", "girlanda", "hvězda", "cukrovinka", "svíčka", "světelný řetěz"]
    
    class Ozdoba:
    
        def __init__(self, typ, barva):
            self.__typ_ozdoby = typ
            self.__barva = barva
            
        def __str__(self):
            return f"{self.__typ_ozdoby}: {self.__barva}"

    def __init__(self, tot):
        self.__typ_stromku = tot if tot in VanocniStrom.typ_stromku else None
        self.__ozdoby = []
        
    def ozdob(self, typ, barva, pocet):
        if typ in VanocniStrom.typ_ozdoby:
            for i in range(0, pocet):
                self.__ozdoby.append(self.Ozdoba(typ, barva))
                
    def __str__(self):
        o = self.__typ_stromku + '\n' + "*"*30
        for i in self.__ozdoby:
            o += '\n' + str(i)
        return o            
            
strom = VanocniStrom("borovice")
strom.ozdob("světelný řetěz", "studená bílá", 1)
strom.ozdob("koule", "červená", 10)
strom.ozdob("koule", "bílá", 10)
strom.ozdob("girlanda", "bílá", 3)
strom.ozdob("girlanda", "červená", 3)
strom.ozdob("cukrovinka", "hnědá", 20)
print(strom)