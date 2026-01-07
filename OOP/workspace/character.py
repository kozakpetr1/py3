# třída - obecný charakter v počítačové hře
class Character:
    
    # seznam přípustných charakterů postav, vlastnost třídy (ne objektu)
    roles = ["obchodník",
             "strážce",
             "léčitel",
             "válečník",
             "druid",
             "čaroděj",
             "vědmák"]

    # magická metoda (konstruktor) volána při vzniku objektu
    # slouží především k inicializaci vlastností objektu
    def __init__(self, name, role):
        self.__name = name
        if role in Character.roles:
            self.__role = role
        else:
            self.__role = None
    
    # magická metoda (destruktor) volaná při zániku objektu        
    def __del__(self):
        print(f"Postava {self.__name} byla odstraněna ze hry.")
        
    # magická metoda - textová reprerezentace objektu
    def __str__(self):
        return f"Role: {self.__role}, Jméno: {self.__name}"
    
# Třída PlayerCharacter je potomkem třídy Character, tzn.
# že dědí metody a vlastnosti třídy Character    
class PlayerCharacter(Character):

    def __init__(self, name, role, control_device):
        # Volání magické metody __init__ rodičovské třídy
        Character.__init__(self, name, role)
        self.__device = control_device
        
    def __str__(self):
        # Volání rodičovské metody pomocí super() 
        return f"{super().__str__()}, Ovládání: {self.__device}"
        

# Objekt npc_character je instancí třídy Character        
npc_character = Character("Stregobor", "čaroděj")

# Objekt zaklinac je instancí třídy PlayerCharacter
zaklinac = PlayerCharacter("Zaklínač", "vědmák", "klávesnice")
# Volání magické metody __str__
print(npc_character)
# Volání magické metody __str__
print(zaklinac)
# zrušení objektů
del npc_character
del zaklinac