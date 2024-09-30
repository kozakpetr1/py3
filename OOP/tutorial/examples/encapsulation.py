class Bird:
    def __init__(self, predator = True):
        self.__predator = predator # private property initialization
    
    def __str__(self):
        return "*"*20 + "\nThis is some bird.\n" + "*"*20

    # setter method to set value of private property __predator
    def setPredator(self, predator = True):
        self.__predator = predator

    # getter method to get value of private property __predator
    def getPredator(self):
        return self.__predator

    def isPredator(self):
        print(f"Predator: {self.__predator}")

class Eagle(Bird):

    def __str__(self):
        return "*"*20 + "\nThis is an eagle.\n" + "*"*20

# B as an instance of Bird class - new object
B = Bird(True)
# call __str__ magic method
print(B)
# call isPredator method
B.isPredator()
# call setter method to set value of private __predator property
# B.__predator = False - this code is incorrect
B.setPredator(False)
# call getter to get value of private__predator property
print("Predator: {}".format(B.getPredator()))

E = Eagle(True)
print(E)
E.isPredator()
E.setPredator(False)
print("Predator: {}".format(E.getPredator()))