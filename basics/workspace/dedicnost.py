class Polygon:
    
    def __init__(self, sides):
        self.__sides = sides
        
    def getSides(self):
        return self.__sides
    
    def setSides(self, sides):
        self.__sides = sides
        
    def __str__(self):
        return "Počet stran polygonu je: " + str(self.getSides())

class Triangle(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 3)

    def __str__(self):
        return super().__str__() + " Trojúhelník má tři strany. Dycky trojúhelník."

class Pentagon(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 5)

    def __str__(self):
        return super().__str__() + " Pentagon má pět stran. Nediv se."

t = Triangle()
print(t)

penta = Pentagon()
print(penta)

p = Polygon(7)
# print(p.__sides) - chybně, nelze volat private vlastnost
print(p.getSides())
# p.__sides = 8 - chybně, nelze volat private vlastnost
p.setSides(8)
print(p.getSides())
print(p)
