class Lady:
    
    # magická metoda - konstruktor
    def __init__(self, h, w, a, sex, status, skin):
        self.height = h
        self.weight = w
        self.age = a
        self.sex = sex
        self.status = status
        self.skin = skin
        
    def about(self):
        s = "Hi! I am " + str(self.age) + ". I am " + self.status + " now. Would You like to date me?"
        return s
        
black_lady = Lady(165, 55, 18, "F", "single", "black")
white_lady = Lady(160, 50, 25, "F", "married", "white")
grey_lady = Lady(170, 25, 90, "F", "dead", "grey")

print(black_lady.status)
print(white_lady.status)
print(grey_lady.status)
print(black_lady.about())
print(white_lady.about())
print(grey_lady.about())