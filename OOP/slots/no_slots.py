class Bod2D:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
bod = Bod2D(1, 3)
print(bod.__dict__)
bod.z = 5
print(bod.__dict__)