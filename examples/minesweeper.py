""" Minesweeper
    Čtvercová hrací plocha o n x n polích.
    X - skryté okno pole
    space - odkryté prázdné okno pole
    M - odkryté okno pole s minou

    Ukázka pole:
       1  2  3  4  5
    1  X  X  X  X
    2  X  X     X  X
    3  X  M  X  X  X
    4  X     X  X  X
    5  X        X  X 
"""
import random
import os

clear = lambda: os.system('cls')

# inicializace pseudogenerátoru náhodných čísel
random.seed()

# proměnná dimension určuje rozměry minového pole dimension x dimension
dimension = 5
# proměnná mineField je dvojrozměrný list o dimension řádcích a dimension sloupcích
# všechny položky dvojrozměrného listu jsou naplněny hodnotou 0
mineField = [[0] * dimension for i in range(dimension)]

""" Funkce setMineField(field, dim = 5) nastraží miny pomocí pseudogenerátoru náhodných čísel.
 
"""
def setMineField(field, dim = 5):
    for i in range(dim):
        for j in range(dim):
            field[i][j] = int(random.random() * 100) % 2

def getItemChar(i):
    items = { 1: "X", 0: "X", -1: "M", -2: " ",-3: "W", -4: "_" }
    return items.get(i, "E")

def getItemVal(i):
    items = { 1: -1, 0: -2, -1: -3, -2: -4, -3: -3, -4: -4 }
    return items.get(i, -5)

    
""" Funkce showMineField(field) zobrazí pole s minami.
 
"""
def showMineField(field):
    for row in field:
        print('  '.join([(getItemChar(elem)) for elem in row]))
        
def uncoverFieldItem(field, row, col, dim = 5):
    if row in range(1, dim + 1) and col in range(1, dim + 1):
#        field[row-1][col-1] = -2 if field[row-1][col-1] == 0 else -1 if field[row-1][col-1] == 1 else field[row-1][col-1]
        field[row-1][col-1] = getItemVal(field[row-1][col-1])
        return field[row-1][col-1]
    else:
        return -5

clear()
setMineField(mineField, dimension)

succAttempt = 0
while True:
    showMineField(mineField)
    row = int(input(f"Zadej číslo řádku od 1 do {dimension}: "))
    col = int(input(f"Zadej číslo sloupce od 1 do {dimension}: "))
    status = uncoverFieldItem(mineField, row, col, dimension)
    if status == -1:
        print("Booooooom! Šlápl jsi na minu.")
        break
    elif status == -3 or status == -4:
        print("Šlápl jsi na již odkryté pole! Zkus to znovu")
    elif status == -5:
        print("Jsi mimo pole! Zkus to znovu.")
    else:
        print('Dobrá trefa! Prázdné pole.')
        succAttempt += 1

showMineField(mineField)
print("Počet úspěšných pokusů: ", succAttempt)
