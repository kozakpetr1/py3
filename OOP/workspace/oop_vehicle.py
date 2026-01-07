class Vehicle:
    
    def __init__(self, model, speed, horse_power):
        self.model = model
        self.speed = speed
        self.horse_power = horse_power
        
    def drive(self, driver):
        return driver + " drives this vehicle."
    
    def crash(self, driver):
        return self.model + " crashed by " + driver + "."

bmw = Vehicle("BMW X6", 250, 200)
print(bmw.drive("Adéla"))
print(bmw.crash("Adéla"))

velorex = Vehicle("Velorex", 50, 16)
print(velorex.drive("Vítek"))
print(velorex.crash("Vítek"))

mustang = Vehicle("Mustang GT", 280, 210)
print(mustang.drive("Oleksandr"))
print(mustang.crash("Oleksandr"))