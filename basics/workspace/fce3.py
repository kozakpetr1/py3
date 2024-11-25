def jsouVanoce(den, mesic):
    if mesic == 12 and (den == 25 or den == 26):
        return f"{den}. {mesic}. jsou Vánoce!"
    else:
        return f"{den}. {mesic}. nejsou Vánoce!"

print(jsouVanoce(23, 12))
print(jsouVanoce(24, 12))
print(jsouVanoce(25, 12))
print(jsouVanoce(26, 12))
print(jsouVanoce(27, 12))

