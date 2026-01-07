class Dog:
    
    count = 0
    suma = 0
    
    def __init__(self, race, sex, age, price):
        self.race = race
        self.sex = sex
        self.age = age
        self.price = price
        Dog.count += 1
        
    def __del__(self):
        Dog.count -= 1
        Dog.suma += self.price
        
        
print(Dog.count)
shiba_inu = Dog("Shiba Inu", "M", 1, 15000)
shi_tzu = Dog("Shi Tzu", "F", 2, 10000)
husky = Dog("Husky", "M", 1, 20000)
chrt = Dog("Chrt", "F", 1, 20000)

print(Dog.count, Dog.suma)
del shiba_inu
del husky
print(Dog.count, Dog.suma)