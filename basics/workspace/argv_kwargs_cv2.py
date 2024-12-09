def kruznice(**kwargs):
    """Výpočet obsahu, obvodu nebo obojího
    """
    pi = 3.14159265358979
    r = kwargs["polomer"]
    o = kwargs["operace"] # O, S, OS
    
    if (o == "O"):
        return 2 * pi * r
    elif (o == "S"):
        return pi * r ** 2
    elif (o == "OS"):
        return [2 * pi * r, pi * r ** 2]
    else:
        return False

obvod_kruznice = kruznice(polomer = 3, operace = "O")
obsah_kruznice = kruznice(polomer = 3, operace = "S")
obsah_obvod_kruznice = kruznice(polomer = 3, operace = "OS")
print(obvod_kruznice, obsah_kruznice, obsah_obvod_kruznice)