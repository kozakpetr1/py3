""" 
    
"""

import os
import math

clear = lambda: os.system('cls')

class Point:
    
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def setCoords(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getCoords(self):
        return (self.getX(), self.getY())

    def __str__(self):
        return f"[{self.getX()},{self.getY()}]"
    
class LineSegment:

    def __init__(self, u=0, v=0, x=0, y=0):
        self.__a = Point(u, v)
        self.__b = Point(x, y)
    
    def setLineSegmentCoords(self, u, v, x, y):
        self.__a.setCoords(u, v)
        self.__b.setCoords(x, y)

    def __str__(self):
        return  f"[{self.__a.getX()},{self.__a.getY()}][{self.__b.getX()},{self.__b.getY()}]"

    def getLineSegmentLength(self):
        return math.sqrt(math.pow(self.__a.getX() - self.__b.getX(), 2) + math.pow(self.__a.getY() - self.__b.getY(), 2))
    
clear()

B = Point()
B.setCoords(1, -2)
print(B)

U = LineSegment(1, 3, 4, -1)
U.setLineSegmentCoords(1, 3, 4, 0)
print(U)
print(f"{U.getLineSegmentLength():.2f}")