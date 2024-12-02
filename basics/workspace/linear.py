# Výpočet kořene lineární rovnice
# ax + b = 0

# vstupní proměnné: a, b
# výstupní proměnná: x

def korenLinRovnice(a, b):
    if a == 0:
        if b == 0:
            return True
        else:
            return False
    else:
        return (-b) / a

a = 0.01
b = 5

print(korenLinRovnice(a, b))