class M:
    
    pi = 3.14159265358979
    e  = 2.71828182882818

    @staticmethod
    def check(func):
        def wrap(args):
            if isinstance(args, int):
                return func(args)
            else:
                raise Exception("This number is not an integer.") 
        return wrap
        
    @staticmethod
    @check
    def abs(num) -> int:
        return num if num > 0 else -num
    
    @staticmethod
    @check
    def isEven(num) -> bool:
        return True if (num % 2) == 0 else False
    
    @staticmethod
    @check
    def isOdd(num) -> bool:
        return not M.isEven(num)

    @staticmethod
    @check
    def isPositive(num) -> bool:
        return True if num == M.abs(num) else False

    @staticmethod
    @check
    def isNegative(num) -> bool:
        return not M.isPositive(num)
    
    @staticmethod
    @check
    def isPrimeNumber(num) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
        
    @staticmethod
    @check
    def isLeapYear(num) -> bool:
        if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
            return True
        else:
            return False    
    
    @staticmethod
    @check
    def isPerfectNumber(num) -> bool:
        abs_num = M.abs(num)
        divisors_sum = sum(i for i in range(1, abs_num) if abs_num % i == 0)
        return divisors_sum == abs_num
    
    @staticmethod
    @check
    def getSumOfDigits(num) -> int:
        abs_num = M.abs(num)
        digit_sum = sum(int(digit) for digit in str(abs_num))
        return digit_sum
    
print(M.pi)
print(M.e)
print(M.getSumOfDigits(372))
print(M.isPerfectNumber(8128))
# print(M.abs(-6))
# print(M.isPerfectNumber(28))