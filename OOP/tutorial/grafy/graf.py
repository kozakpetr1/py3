graf = [
    [0,6,3,0,7],
    [6,0,2,0,0],
    [3,2,0,0,3],
    [0,7,0,0,8],
    [0,0,3,0,0]
]

def je_hrana(z, do):
    return True if graf[z][do] else False

print(je_hrana(0, 4))
print(je_hrana(4, 0))