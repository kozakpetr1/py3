class myClass:
    myStaticVar = 0; # statická proměnná
    
    def __init__(self, vval, sval):
        self.myDynamicVar = vval
        myClass.myStaticVar = sval

    def incrementVal(self):
        myClass.myStaticVar = myClass.myStaticVar + 1

print(myClass.myStaticVar)
C = myClass(5, 4)
print(myClass.myStaticVar)
print(C.myStaticVar)
print(C.myDynamicVar)
C.incrementVal()
print(myClass.myStaticVar)
print(C.myStaticVar)

D = myClass(10, 6)
print(C.myDynamicVar)
print(D.myDynamicVar)
print(C.myStaticVar)
print(D.myStaticVar)
print(myClass.myStaticVar)
