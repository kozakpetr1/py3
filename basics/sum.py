class CeleCislo:

    def __init__(self, cislo):
        self.x = int(cislo)
        self.prvocislo = self.je_prvocislo()
        self.prirozene = self.je_prirozene()

    def je_prirozene(self):
        return True if (self.x > 0) else False

    def je_prvocislo(self):

        if (self.x < 2):
            return False

        if (self.x == 2 or self.x == 3):
            return True

        for i in range(2,int(self.x**0.5)+1):
            if (self.x % i) == 0:
                return False
        return True        

    def __str__(self):
        return f"Číslo {self.x} " + ("je" if self.prirozene else "není") + " přirozené a " + ("je" if self.prvocislo else "není") + " prvočíslo."

c = CeleCislo(2)
print(c)