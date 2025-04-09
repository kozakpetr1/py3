used_points = []
lenghts = []

def getPath(from_point: int, to_point: int, matrix: list, previous_lenght=0, first=True, blacklist=used_points, answers=lenghts):
    max_index = len(matrix) - 1
    if from_point < 0 or from_point > max_index or to_point == from_point or to_point < 0 or to_point > max_index:
        print("Incorrect parameters")
        return 0
    if first == True:
        blacklist.clear()
        answers.clear()
    
    for i in range(max_index+1):
        if i in blacklist:
            continue
        lenght = matrix[from_point][i]
        if lenght <= 0:
            continue
        if i == to_point:
            return previous_lenght + lenght
        blacklist.append(i)
        x = getPath(i, to_point, matrix, previous_lenght+lenght, False)
        if x:
          answers.append(x)
        
    if first == True:
      return min(answers)



# pořadí: Varnsdorf, Děčín, Nový Bor, Liberec, Ústí nad Labem, Česká Lípa, Mělník, Mladá Boleslav, Praha
the_matrix = [
    # V   D   N   L   Ú   Č   M  Ml   P
    # 0   1   2   3   4   5   6   7   8
    [ 0, 43, 22, 41,  0,  0,  0,  0,  0], # V
    [43,  0, 30,  0, 25,  0,  0,  0,  0], # D
    [22, 30,  0,  0,  0,  8,  0,  0,  0], # N
    [41,  0,  0,  0,  0,  0,  0, 51,  0], # L
    [ 0, 25,  0,  0,  0,  0,  0,  0, 90], # Ú
    [ 0,  0,  8,  0,  0,  0,  46, 45, 0], # Č
    [ 0,  0,  0,  0,  0, 46,  0,  0, 39], # M
    [ 0,  0,  0, 51,  0, 45,  0,  0, 67], # Ml
    [ 0,  0,  0,  0, 90,  0, 39, 67,  0]  # P
]

print(getPath(0, 8, the_matrix))