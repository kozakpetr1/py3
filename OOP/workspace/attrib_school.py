class School:
    
    num_of_boys = 0
    num_of_girls = 0
    total_number = 0
    
    def __init__(self, name ,m, f):
        self.class_name = name
        self.boys = m
        self.girls = f
        School.num_of_boys += self.boys
        School.num_of_girls += self.girls
        School.total_number = School.num_of_boys + School.num_of_girls    

    def __del__(self):
        School.num_of_boys -= self.boys
        School.num_of_girls -= self.girls
        School.total_number -= self.boys + self.girls

trida_1A = School("1A", 20, 15)
trida_2A = School("2A", 15, 12)
trida_3A = School("3A", 14, 10)
trida_3B = School("3B", 9, 14)
trida_4A = School("4A", 10, 16)
trida_4B = School("4B", 8, 17)
print(School.num_of_boys)
print(School.num_of_girls)
print(School.total_number)
del trida_1A
print(School.num_of_boys)
print(School.num_of_girls)
print(School.total_number)
