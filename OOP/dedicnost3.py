import os
clear = lambda: os.system('cls')

class Father:
    def __init__(self):
        print("Father")

class Mother:
    def __init__(self):
        print("Mother")
    
class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Child")
        
clear()
   
print("-"*10, "Mother") 
M = Mother()
print("-"*10, "Father") 
F = Father()
print("-"*10, "Child")
C = Child()