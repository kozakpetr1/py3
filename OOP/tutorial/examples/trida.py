class Phone:
    
    def __init__(self, brand, battery, storage, ram, diag_length):
        self.brand = brand
        self.battery = battery
        self.storage = storage
        self.ram = ram
        self.diag_length = diag_length
        
    def __str__(self):
        return f"{self.brand}, {self.battery}, {self.storage}, {self.ram}, {self.diag_length}"

cell_phone_1 = Phone("Nokia 5", "5000 mAh", "32 GB", "2 GB", "5.2")
cell_phone_2 = Phone("Infinix Note 30 Pro", "5000 mAh", "64 GB", "8 GB", "6.7")
print(cell_phone_1)
print(cell_phone_2)
