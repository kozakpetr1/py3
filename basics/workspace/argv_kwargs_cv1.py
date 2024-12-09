"""_summary_
    V Pythonu vytvoř skript, který bude obsahovat funkci
    pocitej(**kwargs), která vrátí v závislosti na vstupních
    argumentech jeden z následujících výpočtů:
    - aritmetický průměr
    - minimum
    - maximum
"""
def pocitej(**kwargs):
    c = kwargs["cisla"] # pole čísel, např. [1, 3, 9, 5, 12]
    o = kwargs["operace"] # min, max, avg
    
    if (o == "min"):
        return min(c)
    elif (o == "max"):
        return max(c)
    elif (o == "avg"):
        return sum(c)/len(c)
    else:
        return False
    
min = pocitej(cisla = [2, 3, 5, 7, 11, 13, 17, 19, 23], operace = "min")
max = pocitej(cisla = [2, 3, 5, 7, 11, 13, 17, 19, 23], operace = "max")
avg = pocitej(cisla = [2, 3, 5, 7, 11, 13, 17, 19, 23], operace = "avg")

print(min, max, avg)