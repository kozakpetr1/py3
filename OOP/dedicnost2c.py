import os
import math

clear = lambda: os.system('cls')

class Bod:
    
    def __init__(self, B: dict):
        self.B = B

    def nastavSouradnice(self, x, y):
        self.B["x"] = x
        self.B["Y"] = y

    def __str__(self):
        return "[{},{}]".format(self.B["x"], self.B["y"])
    
class Usecka:

    def __init__(self, A: Bod, B: Bod):
        self.__a = A
        self.__b = B
    
    def nastavSouradnice(self, A: dict, B: dict):
        self.__a.nastavSouradnice(A["x"], A["y"])
        self.__b.nastavSouradnice(B["x"], B["y"])

    def __str__(self):
        return  "[{},{}][{},{}]".format(self.__a.B["x"], self.__a.B["y"], self.__b.B["x"], self.__b.B["y"])

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.__a.B["x"] - self.__b.B["x"], 2) + math.pow(self.__a.B["y"] - self.__b.B["y"], 2))
    
clear()

B = Bod({"x": 1, "y": -2})
print(B)

D = Bod({"x": 1, "y": 3})
E = Bod({"x": 4, "y": -1})
U = Usecka(D, E)
print(U)
print(f"{U.delkaUsecky():.2f}")