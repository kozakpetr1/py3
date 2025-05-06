import random

class List2d:
    
    def __init__(self, rng = 10):
        
        self.__a = [[random.randint(0, 10) for _ in range(0, rng)] for _ in range(0, rng)]
        self.__b = [[random.randint(0, 10) for _ in range(0, rng)] for _ in range(0, rng)]
        self.__out = None
        self.__rng = rng
        
    def suma(self):
        
        self.__out = None
        self.__out = [[(self.__a[i][j] + self.__b[i][j]) for j in range(0, self.__rng)] for i in range(0, self.__rng)]
        return self.__out
    
    def mult(self):
        
        self.__out = None
        self.__out = [[(self.__a[i][j] * self.__b[i][j]) for j in range(0, self.__rng)] for i in range(0, self.__rng)]
        return self.__out
    
l = List2d()
print(l.suma())
print(l.mult())