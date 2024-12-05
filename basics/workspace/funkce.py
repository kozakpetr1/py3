# Povrch kvádru o stranách a, b, c: S = 2(ab + ac + bc)

a = float(input("Zadej a: "))
b = float(input("Zadej b: "))
c = float(input("Zadej c: "))

S = 2 * (a * b + a * c + b * c)
print(S)

# a1 = 2 * a
# b1 = 2 * b
# c1 = 2 * c
a1, b1, c1 = 2 * a, 2 * b, 2 * c
S1 = 2 * (a1 * b1 + a1 * c1 + b1 * c1)
print(S1)

def povrchKvadru(hrana_a, hrana_b, hrana_c):
    return 2 * (hrana_a * hrana_b + hrana_a * hrana_c + hrana_b * hrana_c)

S2 = povrchKvadru(a, b, c)
print(S2)
S3 = povrchKvadru(2 * a, 2 * b, 2 * c)
print(S3)

def objemKvadru(hrana_a, hrana_b, hrana_c):
    return hrana_a * hrana_b * hrana_c

V = objemKvadru(a, b, c)
print(V)

V1 = objemKvadru(2 * a, 2 * b, 2 * c)
print(V1)

def objemKoule(polomer):
    return (4/3) * 3.14159265358979 * polomer ** 3

Vk_a = objemKoule(a)
Vk_b = objemKoule(b)
Vk_c = objemKoule(c)
print(Vk_a, Vk_b, Vk_c)

def objemValce(polomer_podstavy, vyska_valce):
    return (3.14159265358979 * polomer_podstavy ** 2) * vyska_valce

Vv = objemValce(b, c)
print(Vv)
