from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def whoami(self):
        pass
    
# Vytvoř třídu Giraffe jako potomka třídy Animal.
# Přepiš abstraktní metodu whoami tak, aby
# vypisovala text "I am a giraffe."

class Giraffe(Animal):
    
    def whoami(self):
        print("I'm a giraffe.")
        
# Vytvoř objekt třídy Giraffe a zavolej
# whoami().

g = Giraffe()
g.whoami()