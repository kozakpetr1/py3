print("Porovnání dvou čísel")

numA = int(input("A: "))
numB = int(input("B: "))

print(f"{numA} je větší než {numB}") if numA > numB else None
print(f"{numA} je menší než {numB}") if numA < numB else None
print(f"{numA} je rovno {numB}") if numA == numB else None
