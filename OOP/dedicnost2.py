""" Dědičnost
    Úsečka jako potomek třídy Bod.

"""

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
    
class Usecka(Bod):

    def __init__(self, u=0, v=0, x=0, y=0):
        Bod.__init__(self, x, y)
        # super().__init__(x, y) - Python 3
        self.u = u
        self.v = v
    
    def nastavSouradnice(self, u, v, x, y):
        self.u = u
        self.v = v
        Bod.nastavSouradnice(self, x, y)

    def __str__(self):
        return  f"[{self.u},{self.v}]" + Bod.__str__(self)

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.u - self.x, 2) + math.pow(self.v - self.y, 2))
    
clear()

B = Bod()
B.nastavSouradnice(1, -2)
print(B)

U = Usecka(1, 3, 4, -1)
print(U)
print(f"{U.delkaUsecky():.2f}")