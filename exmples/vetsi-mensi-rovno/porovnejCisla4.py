print("Porovnání dvou čísel")

class porovnaniCisel:

    def __init__(self):
        self.numA = int(input("A: "))
        self.numB = int(input("B: "))
    
    def vetsiMensiRovno(self):
        if self.numA > self.numB:
            print(f"{self.numA} je větší než {self.numB}")
        else:
            if self.numA < self.numB:
                print(f"{self.numA} je menší než {self.numB}")
            else:
                print(f"{self.numA} je rovno {self.numB}")

cisla = porovnaniCisel()
cisla.vetsiMensiRovno()
