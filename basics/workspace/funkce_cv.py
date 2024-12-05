# Studna válcového tvaru má hloubku hs [m], poloměr skruží r [m]
# a vzdálenost hladiny vody od povrchu studny d [m].
# Napiš funkci, která spočítá objem vody ve studni v metrech krychlových.

r = float(input("Zadej poloměr studny: "))
hs = float(input("Zadej výšku studny: "))
d = float(input("Zadej vzdálenost hladiny od povrchu: "))

def objemValce(polomer_podstavy, vyska_valce):
    return (3.14159265358979 * polomer_podstavy ** 2) * vyska_valce

V = objemValce(r, hs - d)
Vs = objemValce(r, hs)
print(f"Studna má maxilmální objem vody {Vs}")
print(f"Ve studni o poloměru {r} m a výšce {hs} m\ns hladinou vody {d} m od povrchu studny\nje {V} metrů krychlových vody.")