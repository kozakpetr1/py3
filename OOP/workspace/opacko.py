# ============================================
# Přehled metod objektu třídy list v Pythonu
# ============================================
# append(x)        – přidá prvek x na konec seznamu
# extend(iter)     – rozšíří seznam o všechny prvky zadaného iterovatelného objektu
# insert(i, x)     – vloží prvek x na pozici i
# remove(x)        – odstraní první výskyt prvku x
# pop([i])         – odstraní a vrátí prvek na pozici i (výchozí je poslední)
# clear()          – vyprázdní seznam
# index(x[, start[, end]]) – vrátí index prvního výskytu prvku x
# count(x)         – vrátí počet výskytů prvku x
# sort(key=None, reverse=False) – seřadí seznam na místě
# reverse()        – otočí pořadí prvků v seznamu
# copy()           – vrátí mělkou kopii seznamu

# ============================================
# Zadání k procvičení
# ============================================

# 1. Vytvoř prázdný seznam a postupně do něj pomocí append() přidej pět čísel zadaných uživatelem.
# 2. Zeptej se uživatele na pět jmen, ulož je do seznamu a následně seznam seřaď abecedně.
# 3. Vytvoř seznam čísel 1–10, pomocí pop() postupně odstraňuj poslední prvky, dokud není seznam prázdný.
# 4. Máš seznam čísel. Pomocí for a if zjisti, kolik čísel je sudých (využij count() pro kontrolu).
# 5. Vytvoř seznam měst, přidej jedno město na začátek pomocí insert().
# 6. Vytvoř seznam [3, 1, 4, 1, 5, 9], zjisti kolikrát se v něm vyskytuje číslo 1 (metoda count).
# 7. Ze seznamu slov odstraň jedno konkrétní slovo (metoda remove). Pokud tam není, vypiš hlášku.
# 8. Zeptej se uživatele na seznam čísel, seřaď je sestupně pomocí sort(reverse=True).
# 9. Vytvoř seznam a pomocí while cyklu vypisuj a zároveň odstraňuj první prvek (pop(0)), dokud není prázdný.
# 10. Vytvoř seznam náhodných čísel a otoč jeho pořadí metodou reverse().
# 11. Vytvoř seznam čísel, zkopíruj jej metodou copy() a s kopií dále pracuj (např. přidej prvky).
# 12. Napiš program, který do seznamu ukládá vstupy uživatele, dokud nezadá „stop“. Poté seznam vypiš.
# 13. Vytvoř seznam čísel a najdi index určitého čísla metodou index(). Pokud číslo neexistuje, vypiš hlášku.
# 14. Máš seznam [2, 4, 6, 8]. Přidej do něj pomocí extend() další seznam [1, 3, 5, 7].
# 15. Vytvoř seznam, do kterého budeš ukládat jen ta čísla od uživatele, která jsou větší než 10 (if + append).
# 16. Máš seznam známek (1–5). Pomocí for spočítej průměr a vypiš jej.
# 17. Vytvoř seznam čísel a vymaž všechny prvky metodou clear(). Ověř, že je prázdný.
# 18. Generuj náhodná čísla do seznamu, dokud se neobjeví číslo 7. Poté cyklus while ukonči a vypiš seznam.
