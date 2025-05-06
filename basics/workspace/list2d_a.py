import random

class List2d:
    
    def __init__(self, rng = 10):
        
        self.__a2d = [[random.randint(-100, 101) for _ in range(0, rng)] for _ in range(0, rng)]
        self.__out = None
        self.__rng = rng
        
    def sortIt(self, revrs = False):
        
        self.__a1d = [element for row in self.__a2d for element in row]
        self.__a1d.sort(reverse = revrs)
        self.__out = None
        self.__out = [self.__a1d[i:i + self.__rng] for i in range(0, len(self.__a1d), self.__rng)]
        return self.__out
    
   
l = List2d()
print(l.sortIt())
print(l.sortIt(True))
