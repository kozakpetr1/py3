def is_even(num):
    return False if num & 0x01 else True

def sum_if_even(a, b):
    if is_even(a) and is_even(b):
        return a + b
    else:
        raise Exception("Vstupní parametry mohou být pouze sudá čísla.")
    
print(sum_if_even(6, 4))
