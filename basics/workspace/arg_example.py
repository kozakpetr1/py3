cukrovi = [
    ["linecká kolečka", 5, 90],
    ["vanilkové rohlíčky manglové", 5, 130],
    ["vanilkové rohlíčky ořechové", 5, 120],
    ["vosí hnízda", 5, 100],
    ["rumové koule", 5, 90],
    ["pracny", 5, 70]
]

def kalkulace(cukrovi):
    pocitadlo = 0
    for c in cukrovi:
        print("Provádím kalkulaci pro", c[0] + "...")
        pocitadlo += c[1] * c[2]
    return pocitadlo

print(kalkulace(cukrovi))