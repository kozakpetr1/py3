""" Proměnné
    Formátovaný výstup

"""

age = 36
height = 1.78

print("I am ", age, ".")
print("I am ", height, "tall.")

print("I am %d." % age)
print("I am %.2f tall." % height)
print("I am %d. I am %.2f tall." % (age, height))

myAge = "I am {}."
myHeight = "I am {} tall."
print(myAge.format(age))
print(myHeight.format(height))

# chyba: print("I am " + age + ".")
print("I am " + str(age) + ".")
print("I am " + str(height) + ".")

print(f"I am {age}. I am {height} tall.")