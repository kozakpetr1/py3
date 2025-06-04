

class WhoAmI:
    
    def __init__(self, name = "John Doe"):
        self.__name = name
        
    def __str__(self):
        return self.__name
    
who_am_i = WhoAmI("Thanos")
print(who_am_i)

print()