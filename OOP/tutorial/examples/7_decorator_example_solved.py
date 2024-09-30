# Návrhové vzory - DECORATOR, FACTORY 
# ---------------------------------------------------------------------
# Uprav kód třídy Cafe takovým způsobem, aby byl ošetřen parametr
# "type" při volání "Cafe.addToMenu()" pomocí dekorátoru "@check_type".
# V případě, že daný typ zboží nelze přidat pomocí faktorky
# "Cafe.addToMenu()", dojde k vyvolání výjimky a objekt není vytvořen.

from abc import ABC, abstractclassmethod

class Coffee(ABC):
    
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    @abstractclassmethod
    def makeCoffee(self):
        pass
    
class Ristretto(Coffee):
    
    def makeCoffee(self):
        print(f"Making {self.size} size ristretto for {self.price} Euro...")

class Cappuccino(Coffee):
    
    def makeCoffee(self):
        print(f"Making {self.size} size cappucino for {self.price} Euro...")

class Espresso(Coffee):
    
    def makeCoffee(self):
        print(f"Making {self.size} size espresso for {self.price} Euro...")

class Cafe:
    
    type = ['Ristretto', 'Cappuccino', 'Espresso']

    @staticmethod
    def check_type(func):
        def wrap(arg1, arg2, arg3):
            if arg1 in Cafe.type:
                return func(arg1, arg2, arg3)
            else:
                raise Exception("This item cannot be added to the menu.")
        return wrap
                
    @staticmethod
    @check_type
    def addToMenu(type, size, price):
        return globals()[type](size, price)

menu = []

menu.append(Cafe.addToMenu('Ristretto', 'S', '2.50'))
menu.append(Cafe.addToMenu('Cappuccino', 'L', '2.30'))
menu.append(Cafe.addToMenu('Cappucino', 'XL', '3.50')) # vyvolání výjimky
menu.append(Cafe.addToMenu('Espresso', 'M', '2.50'))

for coffee in menu:
    coffee.makeCoffee()
