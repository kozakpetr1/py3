a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))

if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
    
print(f"{a}  {b}  {c}")