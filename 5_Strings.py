""" Textové řetězce

"""

myFirstString = "Shit happens. "
print(myFirstString)
print(myFirstString[1])

print(len(myFirstString))

print(myFirstString.upper())
print(myFirstString.lower())
print(myFirstString.strip())
print(myFirstString.replace("Shit", "Nothing"))
print(myFirstString.split(" "))

print("Shit" in myFirstString)
print("shit" in myFirstString)

if "Shit" in myFirstString:
    print("Yes, 'Shit' is present.")
  
for myChar in myFirstString:
    print(myChar)
  
mySecondString = 'Shit happens too. '

multiLine1stString = """I am
sooooo happy."""
print(multiLine1stString)

multiLine2ndString = '''I am
sooooo happy too.'''
print(multiLine2ndString)

# slicing = 'krájení' textu
print(multiLine1stString[:6]) # od začátku do pozice 6 (nezapočítává se)
print(multiLine1stString[2:6]) # od pozice 2 (počítáno od 0) do pozice 6 (nezapočítává se)
print(multiLine1stString[2:]) # od pozice 2 (počítáno od 0) do konce (nezapočítává se)

escString1 = "My name is \"Petr\""
escString2 = 'My name is "Petr"'
escString3 = '\tMy name is "Pete\br"'
escString4 = "\tMy name is \"Pete\br\""
print(escString1)
print(escString2)
print(escString3)
print(escString4)

escString5 = "\tis my name.\r \"Pete\br\""
print(escString5)

specString = "\x23\x20\x48\x69\x21"
specString2 = "\043\040\110\151\041"
print(specString)
print(specString2)