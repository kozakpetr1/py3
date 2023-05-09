i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print ('{: >4}'.format(j * i), end=" ")
        j += 1
    i += 1
    print("")