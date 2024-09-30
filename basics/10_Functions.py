"""Functions
"""

def setVal(a=0):
    return a

def pow(a=1, n=0):
    return a**n

def shwArgs(*args):
    for item in args:
        print(item, end=" ")

b = setVal("Christmas!") # b = "Christmas!"
c = setVal(3) # c = 3
d = setVal() # d = 0

x1 = pow()
x2 = pow(n=3)
x3 = pow(a=2)
x4 = pow(3, 4)
x5 = pow(a=3, n=4)
x6 = pow(n=3, a=4)

shwArgs("Chrome", "Edge", "Firefox", "Opera", "Safari")