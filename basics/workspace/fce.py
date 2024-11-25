def vyresObjemKoule(polomer):

    return (4/3) * 3.14159265358979 * polomer ** 3 if polomer > 0 else False

objem = 1
while objem:
    objem = vyresObjemKoule(float(input("Zadej poloměr koule: ")))
    print(objem)
    
r1, r2, r3 = 17, 3.5, 21.7

print(vyresObjemKoule(r1))
print(vyresObjemKoule(r2))
print(vyresObjemKoule(r3))
