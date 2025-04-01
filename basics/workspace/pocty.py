class Pocty:

    @staticmethod
    def sum(a, b):
        return a + b

    # a * b
    @staticmethod
    def multiply(a, b):
        return a * b

    # a / b
    @staticmethod
    def divide(a, b):
        try:
            return a / b
        except:
            raise ValueError("Dělění nulou.")

    # a na n-tou
    @staticmethod
    def power(a, n):
        return pow(a, n)
        
try:
    x = float(input("Zadej číslo: "))
except:
    raise TypeError("Není číslo.") 

try:
    y = float(input("Zadej číslo: "))
except:
    raise TypeError("Není číslo.") 

z = Pocty.divide(Pocty.sum(Pocty.power(x, 3), -Pocty.multiply(y, x)), Pocty.sum(x, -1))
z2 = (x **3 - y*x) / (x - 1)
print(z)
print(z2)
# vypocet z = (x^3 - y*x) / (x - 1)