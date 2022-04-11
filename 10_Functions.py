"""Functions
"""

def setVal(a):
    return a

def pow(a, n):
    return a**n

def shwArgs(*args):
    for item in args:
        print(item)

b = setVal("Christmas!")
print(b)

x = pow(3,4)
print(x)

shwArgs("Chrome", "Edge", "Firefox", "Opera", "Safari")