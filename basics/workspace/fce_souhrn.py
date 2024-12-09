def slepText(t1, t2):
    return t1 + " " + t2

def slepText2(slova):
    slepenec = ""
    for slovo in slova:
        slepenec = slepenec + slovo + " "
    return slepenec
    
def slepText3(slova):
    return " ".join(slova)

def slepText4(*argv):
    return " ".join(argv)

t1 = "Vánoční"
t2 = "koleda"
t = ["Vánoční", "koleda"]    
print(slepText("Vánoční", "Koleda"))
print(slepText(t1, t2))
print(slepText2(["Vánoční", "Koleda"]))
print(slepText2(t))
print(slepText3(["Přelet", "nad", "kukaččím", "hnízdem"]))
print(slepText4("Přelet", "nad", "kukaččím", "hnízdem"))