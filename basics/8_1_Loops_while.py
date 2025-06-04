def arithmSeq(a1, d, n):
    return a1 + d * (n - 1)

def isEven(num):
    return num % 2 == 0

print("Prvních n-členů aritmetické posloupnosti")
firstMember = float(input("První člen posloupnosti: "))
difference = float(input("Přírůstek: "))
numOfMembers = int(input("Počet členů: "))

i = 1
while i <= numOfMembers:
    print(f"a[{i}]=", arithmSeq(firstMember, difference, i), end=", ")
    i += 1
else:
    print("END")

print("Sudá čísla od 1 do n")
n = int(input("Zadej n: "))
i = 1
while i <= n:
    if isEven(i):
        print(i, end=" ")
    i += 1

i = 0    
while i < 3:
    i += 1
print(i)