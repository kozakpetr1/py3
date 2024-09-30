class Usecka:
    def __init__(self, **kwargs):
        self.__A = (kwargs["x1"], kwargs["y1"])
        self.__B = (kwargs["x2"], kwargs["y2"])
        self.__raster = []
        self.smernice()
        self.rasterizuj()
        
    def smernice(self):
        self.__m = (self.__B[1] - self.__A[1]) / (self.__B[0] - self.__A[0])
        
    def rasterizuj(self):
        self.__raster.append(self.__A)
        i = self.__A[0] + 1
        j = self.__A[1]
        while i < self.__B[0]:
            j += self.__m
            self.__raster.append((i, round(j)))
            i += 1
        self.__raster.append(self.__B)
    
    def __str__(self):
        return f"{self.__raster}"
    
u = Usecka(x1 = 0, y1 = 3, x2 = 6, y2 = 0)
print(u)