""" Collections - lists

"""
import os
clear = lambda: os.system('cls')

def goNext():
    input("Pokračuj stiskem klávesy ENTER.")
    clear()

clear()
# nový list tvoří 5 položek s indexy 0 až 4
myList = ["Audi", "Mercedes", "BMW", "Tesla", "Jaguar"]
# vytvoření nového listu pomocí konstrukturu list
myList2 = list(("Audi", "Mercedes", "BMW", "Tesla", "Jaguar"))

print("Přidání položky do listu myList:")
# metoda append přidá položku/y na konec listu
print("Před: ", myList)
myList.append("Mazda")
print("Po: ", myList)
goNext()

print("Odstranění položek z listu myList2:")
# metoda clear odstraní všechny položky z listu
print("Před: ", myList2)
myList2.clear()
print("Po: ", myList2)
goNext()

print("Zobrazení typu proměnné myList:")
# zobrazení typu proměnné myList
print(type(myList))

print("Zobrazení položek myList s indexem 0 a 3:")
# položky listu jsou indexované od 0
# zobrazení položek listu s indexy 0 a 3
print(myList[0], myList[3])

print("Zobrazení sublistu myList s indexem 2-4:")
# zobrazení vybraného rozsahu položek listu myList
print(myList[2:5])
goNext()

print("Výpis položek myList oddělených mezerami pomocí for loopu:")
# výpis položek listu oddělených mezerami pomocí for loopu
for myItem in myList:
    print(myItem, end=" ")
else:
    print("\n")
goNext()

print("Zobrazení počtu položek v myList:")
# zobrazení počtu položek v listu    
print(len(myList))
goNext()

print("Odstranění položky BMW z listu myList:")
# odstranění položky BMW z listu myList
print("Před: ", myList)
myList.remove("BMW")
print("Po: ", myList)
print(myList)
goNext()

print("Zobrazení indexu vybrané položky v myList:")
# zobrazení indexu vybrané položky v listu
print(myList.index("Tesla"))
goNext()

print("Seřazení položek v myList vzestupně:")
# seřazení položek listu vzestupně
print("Před: ", myList)
myList.sort()
print("Po: ", myList)

print("Seřazení položek v myList sestupně:")
# seřazení položek listu sestupně
print("Před: ", myList)
myList.sort(reverse=True)
print("Po: ", myList)
goNext()

print("Přiřazení kopie listu myList proměnné myList3:")
# přiřazení kopie listu myList proměnné myList3
myList3 = myList.copy()
print(myList3)
goNext()

print("Odstranění položky s vybraným indexem z listu myList3:")
# odstranění položky s vybraným indexem z listu
print("Před: ", myList3)
myList3.pop(0)
print("Po: ", myList3)
goNext()

print("Reverze položek v listu myList3:")
# reverze položek v listu
print("Před: ", myList3)
myList3.reverse()
print("Po: ", myList3)
goNext()

print("Různé typy hodnot v listu difTypesOfValues:")
# list může obsahovat položky různého typu
difTypesOfValues = ["blik", 0, False, 3.5]
print(difTypesOfValues)
print("Stejné hodnoty v listu sameValues:")
# hodnoty v listu se mohou opakovat
sameValues = ["blik", 0, "blik", 3.5]
goNext()

# hodnoty v listu lze změnit po jedné položce
print(myList)
myList[2] = "Trabant"
print(myList)

# hodnoty v listu lze změnit v daném rozsahu položek
myList[0:2] = ["Dacia", "Škoda"]
print(myList)

# přidání položky do listu na vybranou pozici
myList.insert(3, "Velorex")
print(myList)
