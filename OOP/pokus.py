class X:

    pocitadlo = 0
    def __init__(self):
        X.pocitadlo = X.pocitadlo + 1
        
    def __del__(self):
        X.pocitadlo = X.pocitadlo - 1

x1 = X()
print(X.pocitadlo)
x2 = X()
print(X.pocitadlo)
del(x2)
print(X.pocitadlo)    