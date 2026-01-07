class Nuts:
    
    total_weight = 0
    
    def __init__(self, weight):
        self.weight = weight
        Nuts.total_weight += self.weight
        
    def __del__(self):
        Nuts.total_weight -= self.weight

print(Nuts.total_weight) 
order_1 = Nuts(25)
order_2 = Nuts(35)
order_3 = Nuts(15)
order_4 = Nuts(20) 
print(Nuts.total_weight)
del order_2
print(Nuts.total_weight) 
