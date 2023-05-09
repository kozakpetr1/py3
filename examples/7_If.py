""" if statements
    Logické operátory: == != < > <= >=

"""
numA = int(input("Zadej celé číslo A: "))
numB = int(input("Zadej celé číslo B: "))

# if statement
if numA > numB:
    print(f"{numA} > {numB}.")


# if else statement
if numA > numB:
    print(f"{numA} > {numB}.")
else:
    print(f"{numA} <= {numB}.")

# if elif else statement
if numA > numB:
    print(f"{numA} je větší než {numB}.")
elif numA < numB:
    print(f"{numA} je menší než {numB}.")
else:
    print(f"{numA} je rovno {numB}.")

# if else statement jako ternární operátor
print(f"{numA} > {numB}.") if numA > numB else print(f"{numA} <= {numB}.")
print(f"{numA} > {numB}") if numA > numB else print(f"{numA} = {numB}.") if numA == numB else print(f"{numA} < {numB}")

# příklady užití "and or not in" v if statementu 
presents = ["Smartphone", "Barbie", "Nintendo", "Tracksuit", "Slippers"] # list
if "Smartphone" or "iPad" in presents:
    print("I'm sooo happy!")

if not "Tracksuit" and "Socks" in presents:
    print("I'm sooo happy too!")
else:
    print('I hate Christmas!')

# implementace case statementu v Pythonu
def getMonth(monthNum):
    months = {
        1: "leden",
        2: "únor",
        3: "březen",
        4: "duben",
        5: "květen",
        6: "červen",
        7: "červenec",
        8: "srpen",
        9: "září",
        10: "říjen",
        11: "listoped",
        12: "prosinec"
    }
    return months.get(monthNum, "chybné číslo měsíce")

month = int(input("Zadej číslo měsíce od 1 do 12: "))
print(f"Měsíc číslo {month}: ", getMonth(month))