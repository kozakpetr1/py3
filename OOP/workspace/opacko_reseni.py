# ============================================
# Řešení úloh s metodami list a řídícími strukturami
# ============================================

# 1. Vytvoř prázdný seznam a postupně do něj pomocí append() přidej pět čísel zadaných uživatelem.
cisla = []
for i in range(5):
    n = int(input("Zadej číslo: "))
    cisla.append(n)
print("Výsledný seznam:", cisla)


# 2. Zeptej se uživatele na pět jmen, ulož je do seznamu a následně seznam seřaď abecedně.
jmena = []
for i in range(5):
    j = input("Zadej jméno: ")
    jmena.append(j)
jmena.sort()
print("Seřazená jména:", jmena)


# 3. Vytvoř seznam čísel 1–10, pomocí pop() postupně odstraňuj poslední prvky, dokud není seznam prázdný.
cisla = list(range(1, 11))
while cisla:
    print("Odebráno:", cisla.pop(), "| Zbytek:", cisla)


# 4. Máš seznam čísel. Pomocí for a if zjisti, kolik čísel je sudých.
cisla = [3, 6, 7, 2, 9, 10, 4]
suda = 0
for c in cisla:
    if c % 2 == 0:
        suda += 1
print("Počet sudých čísel:", suda)


# 5. Vytvoř seznam měst, přidej jedno město na začátek pomocí insert().
mesta = ["Praha", "Brno", "Ostrava"]
mesta.insert(0, "Plzeň")
print(mesta)


# 6. Vytvoř seznam [3, 1, 4, 1, 5, 9], zjisti kolikrát se v něm vyskytuje číslo 1.
cisla = [3, 1, 4, 1, 5, 9]
print("Číslo 1 se vyskytuje:", cisla.count(1), "x")


# 7. Ze seznamu slov odstraň jedno konkrétní slovo (metoda remove). Pokud tam není, vypiš hlášku.
slova = ["pes", "kočka", "myš"]
slovo = "kočka"
if slovo in slova:
    slova.remove(slovo)
    print("Seznam po odstranění:", slova)
else:
    print("Slovo", slovo, "není v seznamu.")


# 8. Zeptej se uživatele na seznam čísel, seřaď je sestupně pomocí sort(reverse=True).
cisla = [int(x) for x in input("Zadej čísla oddělená mezerou: ").split()]
cisla.sort(reverse=True)
print("Seřazeno sestupně:", cisla)


# 9. Vytvoř seznam a pomocí while cyklu vypisuj a zároveň odstraňuj první prvek (pop(0)), dokud není prázdný.
cisla = [1, 2, 3, 4, 5]
while cisla:
    print("Odebráno:", cisla.pop(0), "| Zbytek:", cisla)


# 10. Vytvoř seznam náhodných čísel a otoč jeho pořadí metodou reverse().
cisla = [2, 5, 8, 1, 9]
cisla.reverse()
print("Otočený seznam:", cisla)


# 11. Vytvoř seznam čísel, zkopíruj jej metodou copy() a s kopií dále pracuj.
cisla = [1, 2, 3]
kopie = cisla.copy()
kopie.append(4)
print("Původní:", cisla)
print("Kopie:", kopie)


# 12. Napiš program, který do seznamu ukládá vstupy uživatele, dokud nezadá „stop“. Poté seznam vypiš.
slova = []
while True:
    s = input("Zadej slovo (stop = konec): ")
    if s == "stop":
        break
    slova.append(s)
print("Zadaná slova:", slova)


# 13. Vytvoř seznam čísel a najdi index určitého čísla metodou index(). Pokud číslo neexistuje, vypiš hlášku.
cisla = [10, 20, 30, 40]
hledane = 30
if hledane in cisla:
    print("Index čísla:", cisla.index(hledane))
else:
    print("Číslo není v seznamu.")


# 14. Máš seznam [2, 4, 6, 8]. Přidej do něj pomocí extend() další seznam [1, 3, 5, 7].
cisla = [2, 4, 6, 8]
cisla.extend([1, 3, 5, 7])
print(cisla)


# 15. Vytvoř seznam, do kterého budeš ukládat jen ta čísla od uživatele, která jsou větší než 10.
vetsi = []
for i in range(5):
    n = int(input("Zadej číslo: "))
    if n > 10:
        vetsi.append(n)
print("Čísla větší než 10:", vetsi)


# 16. Máš seznam známek (1–5). Pomocí for spočítej průměr a vypiš jej.
znamky = [1, 2, 3, 1, 2, 4]
soucet = 0
for z in znamky:
    soucet += z
prumer = soucet / len(znamky)
print("Průměr známek:", prumer)


# 17. Vytvoř seznam čísel a vymaž všechny prvky metodou clear(). Ověř, že je prázdný.
cisla = [1, 2, 3, 4, 5]
cisla.clear()
print("Seznam po clear():", cisla)


# 18. Generuj náhodná čísla do seznamu, dokud se neobjeví číslo 7. Poté cyklus while ukonči.
import random
cisla = []
while True:
    n = random.randint(1, 10)
    cisla.append(n)
    if n == 7:
        break
print("Vygenerovaná čísla:", cisla)
