class myClass:
    myStaticVar = 0; # statická proměnná
    
    def __init__(self, dval, sval):
        self.myDynamicVar = dval # inicializace dynamické proměnné
        myClass.myStaticVar = sval # inicializace statické proměnné

    # inkrementace statické proměnné
    def incStatVal(self):
        myClass.myStaticVar = myClass.myStaticVar + 1

    # inkrementace dynamické proměnné
    def incDynVal(self):
        self.myDynamicVar = self.myDynamicVar + 1

print(myClass.myStaticVar)

A = myClass(5, 4)
print(A.myDynamicVar)
print(A.myStaticVar)
print(myClass.myStaticVar)
A.incStatVal()
print(A.myStaticVar)
print(myClass.myStaticVar)
B = myClass(1, 7)
print(A.myStaticVar)
