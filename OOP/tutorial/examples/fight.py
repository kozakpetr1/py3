class Fighter:
    
    def __init__(self, name, xp = 0):
        self.name = name
        self.xp = int(xp)
        
    def get_xp(self):
        return self.xp
        
class Fight:
    
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2
        
    def go(self):
        if (self.f1.get_xp() > self.f2.get_xp()):
            print(f"Te winner is {self.f1.name}.")
        elif (self.f1.get_xp() < self.f2.get_xp()):
            print(f"The winner is {self.f2.name}.")
        else:
            print(f"Draw.")

fighter_1 = Fighter("Baby Yoda", 2500)
fighter_2 = Fighter("Baby Darth Vader", 2499)
fight = Fight(fighter_1, fighter_2)
fight.go()
print(fighter_1.get_xp(), fighter_2.get_xp())