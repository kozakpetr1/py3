print("Porovnání dvou čísel")

numA = int(input("A: "))
numB = int(input("B: "))

if numA > numB:
    print(f"{numA} je větší než {numB}")
else:
    if numA < numB:
        print(f"{numA} je menší než {numB}")
    else:
        print(f"{numA} je rovno {numB}")
