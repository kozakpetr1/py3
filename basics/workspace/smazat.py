def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def dilatace(image2d):
    rows, cols = len(image2d), len(image2d[0])
    new_image = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            max_val = image2d[i][j]
            if i > 0:
                max_val = max(max_val, image2d[i-1][j])
            if i < rows - 1:
                max_val = max(max_val, image2d[i+1][j])
            if j > 0:
                max_val = max(max_val, image2d[i][j-1])
            if j < cols - 1:
                max_val = max(max_val, image2d[i][j+1])
            new_image[i][j] = max_val
    
    return new_image

def eroze(image2d):
    rows, cols = len(image2d), len(image2d[0])
    new_image = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            min_val = image2d[i][j]
            if i > 0:
                min_val = min(min_val, image2d[i-1][j])
            if i < rows - 1:
                min_val = min(min_val, image2d[i+1][j])
            if j > 0:
                min_val = min(min_val, image2d[i][j-1])
            if j < cols - 1:
                min_val = min(min_val, image2d[i][j+1])
            new_image[i][j] = min_val
    
    return new_image

image2d = [[4 - max(abs(i - 4), abs(j - 4)) for j in range(9)] for i in range(9)]

image_dilatace = dilatace(image2d)
image_eroze = eroze(image_dilatace)
image_eroze2 = eroze(image_eroze)
image_final = dilatace(image_eroze2)


print("Původní matice:")
print_matrix(image2d)
print("Po dilataci:")
print_matrix(image_dilatace)
print("Po první erozi:")
print_matrix(image_eroze)
print("Po druhé erozi:")
print_matrix(image_eroze2)
print("Po finální dilataci:")
print_matrix(image_final)
