class myClass:
    myStaticVar = 0; # statická proměnná
    
    def __init__(self, vval, sval):
        self.myDynamicVar = vval # inicializace dynamické proměnné
        myClass.myStaticVar = sval # inicializace statické proměnné

    # inkrementace statické proměnné
    def incStatVal(self):
        myClass.myStaticVar = myClass.myStaticVar + 1

    def incDynVal(self):
        self.myDynamicVar = self.myDynamicVar + 1


D = myClass(10, 6)
print(C.myDynamicVar)
print(D.myDynamicVar)
print(C.myStaticVar)
print(D.myStaticVar)
print(myClass.myStaticVar)
