a = float(input("Zadej stranu a: "))
b = float(input("Zadej stranu b: "))
c = float(input("Zadej stranu c: "))

if a > b:
    a,b = b,a
if a > c:
    a,c = c,a
if b > c:
    b,c = c,b

if (a + b > c):
    print("Trojúhelník lze sestrojit.")
else:
    print("Trojúhelník nelze sestrojit.")    