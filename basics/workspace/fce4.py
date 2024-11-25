import random

def jakyMamDnesDen():
    if random.randint(0,1) == 1:
        return "dobrý"
    else:
        return "blbý"
    
print (f"Dnes mám {jakyMamDnesDen()} den.")