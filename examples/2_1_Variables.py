""" Proměnné
    Proměnné jsou objekty, datové typy jsou třídy.

"""

age = 36 # celé číslo, proměnná age je objekt třídy int
bodyHeight = float(1.78) # reálné číslo (typ float), proměnná bodyHeight je objekt třídy float
firstName, lastName = "Gal", 'Gadot' 
fullName = firstName + " " + lastName # operace sčítání řetězců
fullName2 = "{} {}" # složené závorky pro formátování řetězce
fullName2.format(firstName, lastName) # metoda format nahradí složené závorky hodnotami proměnných
born = str("Petach Tikva, Izrael") # zadání datového typu proměnné pomocí tzv. castingu
bestKnown = "Wonder Woman" # textový řetězec
about = """
{} is an Israeli actress and model.
At age 18, she was crowned Miss Israel 2004.
She is {} of age and {} tall. She is best known
as {}.
""" # víceřádkový textový řetězec

print(firstName[0])
print(lastName)
print(born)
print(bestKnown)
print(about.format(fullName, str(age), bodyHeight, bestKnown))

print(type(firstName))
print(type(age))
print(type(bodyHeight))