import random

def vyresObjemKoule(polomer):

    return (4/3) * 3.14159265358979 * polomer ** 3 if polomer > 0 else False

objem = 1
while objem:
    objem = vyresObjemKoule(polomer = float(input("Zadej poloměr koule: ")))
    print(objem)

polomery = [random.randint(1, 1000) for i in range(0, 10)]
for i in polomery:
    objem = vyresObjemKoule(i)
    print(objem)