import os
import math

clear = lambda: os.system('cls')

class Bod:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def nastavSouradnice(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"
    
class Usecka:

    def __init__(self, u=0, v=0, x=0, y=0):
        self.__a = Bod(u, v)
        self.__b = Bod(x, y)
    
    def nastavSouradnice(self, u, v, x, y):
        self.__a.x = u
        self.__a.y = v
        self.__b.x = x
        self.__b.y = y

    def __str__(self):
        return  f"[{self.__a.x},{self.__a.y}][{self.__b.x},{self.__b.y}]"

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.__a.x - self.__b.x, 2) + math.pow(self.__a.y - self.__b.y, 2))
    
clear()

B = Bod()
B.nastavSouradnice(1, -2)
print(B)

U = Usecka(1, 3, 4, -1)
print(U)
print(f"{U.delkaUsecky():.2f}")