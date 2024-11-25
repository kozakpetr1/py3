def obsahKruhu(polomer):
    r = float(polomer)
    if r > 0:
        return 3.14159265358979 * r * r
    else:
        return False

def obvodKruhu(polomer):
    r = float(polomer)
    if r > 0:
        return 2 * 3.14159265358979 * r
    else:
        return False

s = obsahKruhu(17.1)
print(s)

o = obvodKruhu(17.1)
print(o)