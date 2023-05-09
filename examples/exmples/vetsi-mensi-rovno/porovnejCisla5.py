print("Porovnání dvou čísel")

class Cislo:

    def __init__(self):
        try:
            self.num = int(input("Zadej cislo: "))
        except: #handle other exceptions such as attribute errors
            self.num = 0
    
    def getNum(self):
        return self.num

class porovnaniCisel:

    def __init__(self, A: Cislo, B: Cislo):
        self.numA = A.getNum()
        self.numB = B.getNum()
    
    def vetsiMensiRovno(self):
        if self.numA > self.numB:
            print(f"{self.numA} je větší než {self.numB}")
        else:
            if self.numA < self.numB:
                print(f"{self.numA} je menší než {self.numB}")
            else:
                print(f"{self.numA} je rovno {self.numB}")

cisloA = Cislo()
cisloB = Cislo()
cisloC = Cislo()

porovnani1 = porovnaniCisel(cisloA, cisloB)
porovnani1.vetsiMensiRovno()

porovnani2 = porovnaniCisel(cisloA, cisloC)
porovnani2.vetsiMensiRovno()

porovnani3 = porovnaniCisel(cisloB, cisloC)
porovnani3.vetsiMensiRovno()
