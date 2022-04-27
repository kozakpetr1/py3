import os
clear = lambda: os.system('cls')

class Father:
    x = 50
    def __init__(self):
        print("Father", self.x)

class Mother:
    x = 40
    def __init__(self):
        print("Mother", self.x)
    
class Child(Father, Mother):
    x = 10
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Child", self.x)
        
clear()
   
print("-"*10, "Mother") 
M = Mother()
print("-"*10, "Father") 
F = Father()
print("-"*10, "Child")
C = Child()