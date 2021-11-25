""" Booleans
    Vyhodnocování výrazů
"""

print("10 > 9 seems to be", 10 > 9)
print("10 == 9 seems to be", 10 == 9)
print("10 < 9 seems to be", 10 < 9)

myIQ = 120
yourIQ = int(input("Type your IQ: "))

if myIQ > yourIQ:
    print("My IQ is greater then your IQ.")
else:
    print("Impossible!")

print("-1 evaluates to", bool(-1))
print("0 evaluates to", bool(0))
print("1 evaluates to", bool(1))
print("ABC evaluates to", bool("ABC"))
print("False evaluates to", bool(False))
print("True evaluates to", bool(True))
print("None evaluates to", bool(None))
print("Empty string evaluates to", bool(""))

def myFunction():
    return True

if myFunction():
    print("Yep! It's true!")
else:
    print("Nope! It's false!")

def isGreater(a, b):
    return a > b

numA = int(input("Type A: "))
numB = int(input("Type B: "))
if isGreater(numA, numB):
    print(f"Yep! {numA} is greater then {numB}!")
else:
    print(f"Nope! {numA} is not greater then {numB}!")

def isInRange(num, min, max):
    return num >= min and num <= max

num = int(input("Type number: "))
min = int(input("Type minimum: "))
max = int(input("Type maximum: "))
if isInRange(num, min, max):
    print(f"Yep! {num} is in <{min},{max}> range!")
else:
    print(f"Nope! {num} is not in <{min},{max}> range!")