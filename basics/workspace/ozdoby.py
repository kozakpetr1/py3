pocet_rad = int(input("Zadej počet řad: "))

prvni_rada = 1
q = 2

S = int(prvni_rada * (1 - q ** pocet_rad) / (1 - q)) # vzorec pro součet prvních n-členů geometrické posloupnosti
print(f"Počet ozdob je {S}")

pocet_kouli = 0
for i in range(pocet_rad):
    pocet_kouli += 2 ** i

print(f"Počet ozdob je {pocet_kouli}")
