class Usecka:
    def __init__(self, **kwargs):
        self.__A, self.__B = (kwargs["x1"], kwargs["y1"]), (kwargs["x2"], kwargs["y2"])
        self.__raster = []
        self.__dy, self.__dx = self.__B[1] - self.__A[1], self.__B[0] - self.__A[0]
        self.__p = 2 * self.__dy - self.__dx
        self.rasterizuj()
        
    def predikuj(self):
        if self.__p >= 0:
            self.__prirustek = 1
            self.__p = self.__p + 2 * self.__dy - 2 * self.__dx
        else:
            self.__prirustek = 0
            self.__p = self.__p + 2 * self.__dy
        return self.__prirustek

    def rasterizuj(self):
        self.__raster.append(self.__A)
        i = self.__A[0] + 1
        j = self.__A[1]
        while i < self.__B[0]:
            j += self.predikuj()
            self.__raster.append((i, round(j)))
            i += 1
        self.__raster.append(self.__B)
    
    def __str__(self):
        return f"{self.__raster}"
    
u = Usecka(x1 = 1, y1 = 2, x2 = 15, y2 = 4)
print(u)