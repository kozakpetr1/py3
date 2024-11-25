class Dog:
    
    def __init__(self):
        pass
    
    def bark(self):
        print("I generally bark because I'm a general dog.")
    
    def eat(self):
        print("I generally eat 'cause I'm a general dog.")
    
    def run(self):
        print("I run as a general dog.")
    
class Bulldog(Dog):
    
    def bark(self):
        super().bark()
        print("Woof woof, You're dead hooman. Woof!!!")
        
    def eat(self):
        super().eat()
        print("I also eat as a bulldog 'cause I actually am bulldog.")
        
    def run(self):
        super().run()
        print("Run hooman 'cause I am very fast.")
        
d = Dog()
d.bark()
d.eat()
d.run()

print("*"*20)

b = Bulldog()
b.bark()
b.eat()
b.run()