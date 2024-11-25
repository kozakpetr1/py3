from abc import ABC, abstractmethod

class Polygon(ABC):
    '''Abstraktní třída pro mnohoúhelník
    '''
    @abstractmethod
    def numofsides(self):
        '''Abstraktní metoda pro počet stran mnohoúhelníku
        '''
        pass
    
class Triangle(Polygon):
        
    def numofsides(self):
        print("I have 3 sides.")

class Pentagon(Polygon):
    
    def numofsides(self):
        print("I have 5 sides.")

class Octagon(Polygon):
    
    def numofsides(self):
        print("I have 8 sides.")
    
t = Triangle()
t.numofsides()

p = Pentagon()
p.numofsides()

o = Octagon()
o.numofsides()