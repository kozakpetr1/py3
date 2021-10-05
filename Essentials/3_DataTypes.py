""" Vestavěné datové typy

Textový typ:	str
Číselné typy:	int, float, complex
Sekvenční typy:	list, tuple, range
Mapovací typy:	dict
Množinové typy:	set, frozenset
Boolean typ:	bool
Binární Typy:	bytes, bytearray, memoryview
"""
s = "Hello World!" # str = textový řetězec (pole znaků)
print(s, "-", type(s))

n = 20 # int = celé číslo
print(n, "-", type(n))

r = 3.14 # float = reálné číslo.
print(r, "-", type(r))

c = 1j # complex = komplexní číslo
print(c, "-", type(c))

myList = ["Thor", "Thanos", "Loki"] # list = seznam
print(myList, "-", type(myList))

myTuple = ("Thor", "Thanos", "Loki") # tuple = n-tice
print(myTuple, "-", type(myTuple))

myRange = range(10) # range = řada, rozsah
for i in myRange:
    print(i)
print(myRange, "-", type(myRange))

myDict = {"Hrom" : "Thor", "Titan" : "Thanos", "Lest" : "Loki"} # dict = slovník
print(myDict, "-", type(myDict))

mySet = {"Thor", "Thanos", "Loki"} # set = sada
print(mySet, "-", type(mySet))

myFrozenSet = frozenset({"Thor", "Thanos", "Loki"}) # frozenset
print(myFrozenSet, "-", type(myFrozenSet))

myBool = False # bool = logický datový typ --> True /False
print(myBool, "-", type(myBool))

myBytes = b"What?" # bytes
print(myBytes, "-", type(myBytes))

myByteArray = bytearray(10) # bytearray
print(myByteArray, "-", type(myByteArray))