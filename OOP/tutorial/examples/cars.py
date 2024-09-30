class Car:
    
    def __init__(self, brand, chassis, engine, color):
        self.brand = brand
        self.chassis = chassis
        self.engine = engine
        self.color = color
        
    def __str__(self):
        return f"{self.brand}, {self.chassis}, {self.engine}, {self.color}"
    
    def set_color(self, new_color):
        self.color = new_color
        
    def set_engine(self, new_engine):
        self.engine = new_engine
        
    def get_color(self):
        return self.color

cars = [
    Car("Honda Civic", "hatchback", "1.6i", "white"),
    Car("Mazda MX5", "coupe", "1.6i", "red"),
    Car("Porsche Taycan", "sedan", "kafemlejnek", "blue")
]

print(cars[1])
print(cars[1].get_color())

cars[1].set_color("blue")

print(cars[1])
print(cars[1].get_color())

