""" Collections - tuples (n-tice)
    - položky jsou indexovány
    - položky mají jasně definované a neměnitelné pořadí
    - po vytvoření n-tice, nelze přidávat, odstraňovat ani měnit položky
    - n-tice mohou být extrahovány do proměnných
    
"""
import os
clear = lambda: os.system('cls')

def goNext():
    input("Pokračuj stiskem klávesy ENTER.")
    clear()

clear()
# nová n-tice tvoří 5 položek s indexy 0 až 4
myTuple = ("Audi", "Mercedes", "BMW", "Tesla", "Jaguar")
# vytvoření nové n-tice pomocí konstrukturu tuple
myTuple2 = tuple(("Audi", "Mercedes", "BMW", "Tesla", "Jaguar"))

print("Přidání položky do n-tice myTuple nelze provést přímo:")
# stejným způsobem lze provést např. odstranění položky z n-tice
# metoda append přidá položku/y na konec listu
print("Před: ", myTuple)
myList = list(myTuple)
myList.append("Mazda")
myTuple = tuple(myList)
print("Po: ", myTuple)
goNext()

print("Odstranění položek z n-tice myTuple2 nelze provést přímo, n-tice nemají metodu clear:")
# metoda clear odstraní všechny položky z listu
print("Před: ", myTuple2)
myTuple2 = ()
print("Po: ", myTuple2)
goNext()

print("Zobrazení typu proměnné myTuple:")
# zobrazení typu proměnné myList
print(type(myTuple))

print("Zobrazení položek myTuple s indexem 0 a 3:")
# položky n-tice jsou indexované od 0
# zobrazení položek n-tice s indexy 0 a 3
print(myTuple[0], myTuple[3])

print("Zobrazení sub n-tice myTuple s indexem 2-4:")
# zobrazení vybraného rozsahu položek n-tice myTuple
print(myTuple[2:5])
goNext()

print("Výpis položek myTuple oddělených mezerami pomocí for loopu:")
# výpis položek n-tice oddělených mezerami pomocí for loopu
for myItem in myTuple:
    print(myItem, end=" ")
else:
    print("\n")
goNext()

print("Zobrazení počtu položek v myTuple:")
# zobrazení počtu položek v n-tici    
print(len(myTuple))
goNext()

print("Zobrazení indexu vybrané položky v myTuple:")
# zobrazení indexu vybrané položky v n-tici
print(myTuple.index("Tesla"))
goNext()

print("Různé typy hodnot v n-tici difTypesOfValues:")
# n-tice může obsahovat položky různého typu
difTypesOfValues = ("blik", 0, False, 3.5)
print(difTypesOfValues)
print("Opakující se  hodnoty v n-tici sameValues:")
# hodnoty v n-tici se mohou opakovat
sameValues = ("blik", 0, "blik", 3.5)
print(sameValues)
goNext()

# zobrazení počtu výskytů zadané položky v n-tici
print(sameValues.count("blik"))

# extrahování n-tice do proměnných
myVehicles = ("Bike", "Skateboard", "Tricycle")
vehicle1, vehicle2, vehicle3 = myVehicles
print(vehicle1)
print(vehicle2)
print(vehicle3)
goNext()