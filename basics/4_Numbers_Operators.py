""" Čísla a operace nad čísly

"""

# Celá čísla
print(107) # decimal - 107
print(0o153) # octal - 107
print(0x6B) # hexadecimal - 107
print(0b1101011) # binary - 107
print(0x69 + 0b10) # součet hex. a bin. čísla - 107

print(hex(107)) # 0x6b
print(oct(107)) # 0o153
print(bin(107)) # 0b1101011

print(3.14)
print(0.314E1) # semilogaritmický tvar: základ = 0.314, mantisa = 10, exponent = 1
print(.314e1) # semilogaritmický tvar: základ = 0.314, mantisa = 10, exponent = 1

# ARITMETICKÉ OPERÁTORY
# U operací záleží na typu argumentů
print(5 + 3)   # 8 - int
print(5 + 3.0) # 8.0 - float
print(5 * 3)   # 15 - int
print(5 * 3.0) # 15.0 - float
print(5 / 3)   # 1.6666666666666667 - float
print(5 / 3.0) # 1.6666666666666667 - float
print(5 // 3)  # celočíselné dělení: 1 - int
print(5 // 3.0)# celočíselné dělení: 1.0 - float
print(5 % 3)   # zbytek po dělení: 2 - int
print(5 % 3.0) # zbytek po dělení: 2.0 - float
print(5 ** 3) # umocňování: 125 - int
print(5 ** 0.5) # odmocnina z 5 - float
print(5 ** (-1)) # 1/5 - float

# OPERÁTORY PŘIŘAZENÍ
num = 10 # proměnné num přiřaď hodnotu 10
num += 2 # num = num + 2
num -= 3 # num = num - 3
num *= 4 # num = num * 4
num /= 3 # num = num / 3
num %= 7 # num = num % 7
num //= 2 # num = num // 2
num **= 4 # num = num ** 4
print(num)

# OPERÁTORY PŘIŘAZENÍ - bitové operátory
numInt = 25
numInt <<= 1 # num = num << 1 eq num = num * 2
print(numInt)
numInt >>= 2 # num = num << 1 eq num = num // 4
print(numInt)

# bitové AND
# -------------------
# | AND |  0  |  1  |
# -------------------
# |  0  |  0  |  0  |
# |  1  |  0  |  1  |
numBitwise = 6
numBitwise &= 3
print(numBitwise)

# bitové OR
# -------------------
# | OR  |  0  |  1  |
# -------------------
# |  0  |  0  |  1  |
# |  1  |  1  |  1  |
numBitwise = 6
numBitwise |= 3
print(numBitwise)

# bitové XOR
# -------------------
# | XOR |  0  |  1  |
# -------------------
# |  0  |  0  |  1  |
# |  1  |  1  |  0  |
numBitwise = 6
numBitwise ^= 3
print(numBitwise)

# bitové NOT - inverze bitů
# -------------------
# | NOT |  0  |  1  |
# -------------------
# |     |  1  |  0  |
numBitwise = ~numBitwise
print(numBitwise)
