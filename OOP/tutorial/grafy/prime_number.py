def is_prime(num):
    d = round(num ** 0.5) + 1
    for i in range(2, d):
        if num % i == 0:
            return False
    return True

def sum_of_primes(begin, end):
    pass

for j in range(2, 100):
    if is_prime(j):
        print(j, end=" ")
