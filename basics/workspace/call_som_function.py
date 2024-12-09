def nejaka_funkce():
    print("Ahoj")

def zavolej_nejakou_funkci(funkce):
    globals()[funkce]()
    
zavolej_nejakou_funkci("nejaka_funkce")