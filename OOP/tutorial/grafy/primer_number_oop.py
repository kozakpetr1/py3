class prime:
    def __init__(self):
        self._s = 0
        self._d = 0
        
    def is_prime(self, num):
        self._d = round(num ** 0.5) + 1
        for i in range(2, self._d):
            if num % i == 0:
                return False
        return True

    def sum_of_primes(self, begin, end):
        for j in range(begin, end):
            if self.is_prime(j):
                self._s += j
        return self._s 

p = prime()
print(p.sum_of_primes(2, 100))