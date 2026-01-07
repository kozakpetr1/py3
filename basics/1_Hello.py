def je_prvocislo(x):
    return x > 1 and all(x % i for i in range(2, int(x**0.5)+1))

n = int(input("Zadej cisslo > 0: "))
suda = licha = prvocisla = 0

for i in range(1, n+1):
    if i % 2 == 0: suda += 1; sl = "sudé"
    else: licha += 1; sl = "liché"
    d3 = "dělit. 3" if i % 3 == 0 else "nedělit. 3"
    pr = je_prvocislo(i)
    if pr: prvocisla += 1
    print(f"{i}: {sl}, {d3}, {'je prvočíslo' if pr else 'není prvočíslo'}")

print(f"\nSouhrn:\nSudých: {suda}\nLichých: {licha}\nPrvočísel: {prvocisla}")