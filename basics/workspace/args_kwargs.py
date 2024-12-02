def sectiCisla(a=0, b=0):
    return a + b

print(sectiCisla(sectiCisla(5, 3), -2))
print(sectiCisla())

# Proměnný počet vstupních neklíčových (nepojmenovaných) argumentů funkce - *argv
def sectiCisla2(*argv):
    soucet = 0
    for arg in argv:
        # soucet = soucet + arg
        soucet += arg # += je operátor přičítání
    return soucet

print(sectiCisla2(5, 3, -2))       
print(sectiCisla2(5, 3, -2, 7, 11, 9)) 
print(sectiCisla2())

# Proměnný počet vstupních klíčových (pojmenovaných) argumentů funkce - **kwargs
def sectiCisla3(**kwargs):
    soucet = 0
    for klic, hodnota in kwargs.items():
        soucet += hodnota
    return soucet

print(sectiCisla3(a=5, kocka=3, pes=17, rybicky=25))

def kalkulace(**kwargs):
    # linecke, rohlicky, hnizda, kokosky, koule
    # 80, 65, 90, 45, 120 / 100 g
    # na vstupu bude počet * 100 g
    x = 0
    if "linecke" in kwargs.keys():
        x += 80 * kwargs["linecke"]
    if "rohlicky" in kwargs.keys():
        x += 65 * kwargs["rohlicky"]
    if "hnizda" in kwargs.keys():
        x += 90 * kwargs["hnizda"]
    if "kokosky" in kwargs.keys():
        x += 45 * kwargs["kokosky"]
    if "koule" in kwargs.keys():
        x += 120 * kwargs["koule"]
    return x

def kalkulace2(**kwargs):
    # [<mnozstvi>, <cena za 100 g>]
    print(kwargs)
    pocitadlo = 0
    for klic, hodnota in kwargs.items():
        print("Počítám cenu za: ", klic)
        pocitadlo += hodnota[0] * hodnota[1]
    return pocitadlo
    
print(kalkulace(koule = 5, hnizda = 10, pernicky = 7))
print(kalkulace2(linecke = [5, 80], rohlicky = [7.5, 65], pernicky = [10, 75]))