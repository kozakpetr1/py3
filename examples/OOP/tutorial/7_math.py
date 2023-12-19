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
    def abs(num) -> bool:
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
        pass
        
    @staticmethod
    @check
    def isLeapYear(num) -> bool:
        pass
    
    @staticmethod
    @check
    def isPerfectNumber(num) -> bool:
        pass
    
    @staticmethod
    @check
    def getSumOfDigits(num) -> int:
        pass
    
print(M.abs(-6))