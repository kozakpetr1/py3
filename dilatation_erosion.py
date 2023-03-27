import random
import os
import numpy as np

clear = lambda: os.system('cls')

random.seed()
dimension = 5

def setField():
    global Field, dimension
    Field = [[random.randint(1, 10) for i in range(dimension)] for j in range(dimension)]

def showField(field):
    print(np.matrix(field))

def dilatationField(field, dim = 5):
    for i in range(dim):
        for j in range(dim):
            field[i][j] = field[i][j] + 1 if (field[i][j] < 10) else field[i][j]
            
def erosionField(field, dim = 5):
    for i in range(dim):
        for j in range(dim):
            field[i][j] = field[i][j] - 1 if (field[i][j] > 1) else field[i][j]

clear()
setField()
showField(Field)
dilatationField(Field, dimension)
showField(Field)
erosionField(Field, dimension)
showField(Field)