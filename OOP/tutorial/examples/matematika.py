class Calc:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def sum(self):
        return self.a + self.b
    
    def diff(self):
        return self.a - self.b
    
    def multi(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    
    def set_a(self, new_value):
        self.a = new_value
        
    def set_b(self, new_value):
        self.b = new_value

c = Calc(3, -7)
print(c.multi())

c.set_a(5)
print(c.multi())

c.set_b(4)
print(c.multi())
