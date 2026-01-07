from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def whoami(self):
        pass
    
    @abstractmethod
    def max_speed(self):
        pass

    @abstractmethod
    def fuel(self):
        pass

# Vytvoř třídu Bugatti jako potomka třídy Vehicle.
# Přepiš abstraktní metody whoami, max_speed a fuel.

        
# Vytvoř objekt třídy Bugatti a zavolej metody whoami, max_speed a fuel.
# whoami().

