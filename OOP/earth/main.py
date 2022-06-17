import math as m
import numpy as n

class Coords:

    def __init__(self, lt: dict = {"deg": 0, "min": 0, "sec": 0}, ln: dict = {"deg": 0, "min": 0, "sec": 0}):
        self.__lt, self.__ln = lt, ln
    
    def coordsToRad(self):
        return [n.deg2rad(self.__lt["deg"] + self.__lt["min"] / 60 + self.__lt["sec"] / 3600), n.deg2rad(self.__ln["deg"] + self.__ln["min"] / 60 + self.__ln["sec"] / 3600)]
    
class sphericDistance:
    
    def __init__(self, A: Coords, B: Coords):
        self.__A, self.__B = A, B
        self.__earthRadius = 6371
    
    def __str__(self):
        lt1, ln1 = self.__A.coordsToRad()
        lt2, ln2 = self.__B.coordsToRad()
        return str(m.acos(m.sin(lt1) * m.sin(lt2) + m.cos(lt1) * m.cos(lt2) * m.cos(ln1 - ln2)) * self.__earthRadius)
    
Varnsdorf = Coords({"deg": 50, "min": 55, "sec": 9.532059647628}, {"deg": 14, "min": 38, "sec": 0.9038892957108})
Liberec = Coords({"deg": 50, "min": 46, "sec": 14.651838432012}, {"deg": 15, "min": 3, "sec": 49.4869680093348})
D = sphericDistance(Varnsdorf, Liberec)
print(f"Distance: {D} km")
