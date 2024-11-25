a = float(input("Zadej stranu a: "))
b = float(input("Zadej stranu b: "))
c = float(input("Zadej stranu c: "))

if ((a + b > c) and (b + c > a) and (a + c > b)):
    print("Trojúhelník lze sestrojit.")
else:
    print("Trojúhelník nelze sestrojit.")    