import random

thanos = random.randint(1, 3)
bn = { "kamen": 1, "nuzky": 2, "papir": 3 }
you = input("kamen, nuzky, nebo papir?")

print("thanos: ", list(bn)[thanos-1])
print("you: ", you)

winner = 3 if thanos == bn[you] else thanos & bn[you]

match winner:
    case 0 : print("kamen")
    case 1 : print("papir")
    case 2 : print("nuzky")
    case 3 : print("remiza")
    case other : print("error")