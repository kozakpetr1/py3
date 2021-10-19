""" Proměnné
    Terminálový vstup

"""

# string input
ageString = input("How old are you? ")
print(ageString)
print(type(ageString)) # <class 'str'> !!!

# int input
ageInt = int(input("How old are you? "))
print(ageInt)
print(type(ageInt))

# handling exceptions - zachytávání výjimek
while True:
    try:
        ageInt2 = int(input("How old are you? "))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")