def posunX(bod, posun_X) -> list:    
    return [bod[0] + posun_X, bod[1]]

def posunY(bod, posun_Y) -> list:
    return [bod[0], bod[1] + posun_Y]

def posunBod(bod, posun_X, posun_Y):
    bod_po_posunu_X = posunX(bod, posun_X)
    vysledny_bod = posunY(bod_po_posunu_X, posun_Y)
    return vysledny_bod

def posunBod2(bod, posun_X, posun_Y):
    return [bod[0] + posun_X, bod[1] + posun_Y]
    
A = [3, 7]
B = posunX(A, -2)
print(B)
C = posunY(A, -5)
print(C)
D = posunBod(A, -2, -5)
print(D)
E = posunBod2(A, -2, -5)
print(E)
