class Polygon:
    
    def numOfSides(self):
        pass
    
class Triangle(Polygon):
    
    def numOfSides(self):
        print("Hi! My name is Triangle. I've got 3 sides.")

class Pentagon(Polygon):
    
    def numOfSides(self):
        print("Hi! My name is Pentagon. I've got 5 sides.")

class Octagon(Polygon):
    
    def numOfSides(self):
        print("Hi! My name is Octagon. I've got 8 sides.")

triangle = Triangle()
triangle.numOfSides()

pentagon = Pentagon()
pentagon.numOfSides()

octagon = Octagon()
octagon.numOfSides()