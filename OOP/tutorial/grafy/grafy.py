graf_a = [
    [0,1,0,0,0,0,0,0,0],
    [1,0,3,2,0,0,0,0,0],
    [0,3,0,0,4,0,0,0,0],
    [0,0,0,0,0,0,2,3,0],
    [0,0,4,0,0,2,0,0,0],
    [0,0,0,0,2,0,0,0,3],
    [0,0,0,2,0,0,1,0,0],
    [2,0,0,3,0,2,2,0,0],
    [0,0,2,0,0,3,0,0,0]
]

graf_b = [
    [0,1,0,0,0,0,0,0,0],
    [1,0,1,1,0,0,0,0,0],
    [0,1,0,0,1,0,0,0,0],
    [0,0,0,0,0,0,1,1,0],
    [0,0,1,0,0,1,0,0,0],
    [0,0,0,0,1,0,0,0,1],
    [0,0,0,1,0,0,1,0,0],
    [1,0,0,1,0,1,1,0,0],
    [0,0,1,0,0,1,0,0,0]
]

def je_hrana(graf, zdroj, cil):
    return True if graf[zdroj][cil] else False

def je_obousmerna(graf, uzel1, uzel2):
    return True if je_hrana(graf, uzel1, uzel2) and je_hrana(graf, uzel2, uzel1) else False

def najdi_cestu(graf, zdroj, cil):
    pass
    

print(je_hrana(graf_a, 0, 1))
print(je_hrana(graf_a, 1, 0))
print(je_obousmerna(graf_a, 0, 1))

print(je_hrana(graf_b, 0, 7))
print(je_hrana(graf_b, 7, 0))
print(je_obousmerna(graf_b, 0, 7))