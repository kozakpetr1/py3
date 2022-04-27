import os

clear = lambda: os.system('cls')

class Pes:

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return f"Pes se jmenuje {self.jmeno} a je mu {self.vek}."
    
    def zastekej(self, zvuk="haf"):
        return f"Pes {self.jmeno} štěká {zvuk}."

class Maltezak(Pes):

    def zastekej(self, zvuk="hafi hafi hafi"):
        return Pes.zastekej(self, zvuk) + f" Maltézký psík {self.jmeno} štěká {zvuk}."

class Bulldog(Pes):

    pass

clear()

print("-"*40, "Instance třídy Pes", "-"*40)
vorisek = Pes("Vořech", 5)
print(vorisek)
print(vorisek.zastekej())
print(vorisek.zastekej("woof"))

print("-"*40, "Instance třídy Maltezak", "-"*40)
vivinka = Maltezak("Violka", 2)
print(vivinka)
print(vivinka.zastekej())
print(vivinka.zastekej("wrrr haf"))

print("-"*40, "Instance třídy Bulldog", "-"*40)
brok = Bulldog("Brok", 7)
print(brok)
print(brok.zastekej())
print(brok.zastekej("wrrrrrrr woof wooof woooof wrrrrrrr"))

print("-"*40, "Je objekt instancí třídy", "-"*40)
if isinstance(vorisek, Pes): print(f"{vorisek.jmeno} je Pes.")
if isinstance(vorisek, Maltezak): print(f"{vorisek.jmeno} je Maltezak.")
if isinstance(vorisek, Bulldog): print(f"{vorisek.jmeno} je Bulldog.")
if isinstance(vivinka, Pes): print(f"{vivinka.jmeno} je Pes.")
if isinstance(vivinka, Maltezak): print(f"{vivinka.jmeno} je Maltezak.")
if isinstance(vivinka, Bulldog): print(f"{vivinka.jmeno} je Bulldog.")
if isinstance(brok, Pes): print(f"{brok.jmeno} je Pes.")
if isinstance(brok, Maltezak): print(f"{brok.jmeno} je Maltezak.")
if isinstance(brok, Bulldog): print(f"{brok.jmeno} je Bulldog.")

