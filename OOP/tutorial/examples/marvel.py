class Character:
    
    def __init__(self, name, universe, power):
        self.character_name = name
        self.character_universe = universe
        self.character_power = power
        
    def __str__(self):
        return f"{self.character_name}, {self.character_universe}, {self.character_power}"
    
ch = Character("Thor", "Marvel", "Mjölnir")
ch2 = Character("Spiderman", "Marvel", "cobweb")

print(ch)
print(ch2)