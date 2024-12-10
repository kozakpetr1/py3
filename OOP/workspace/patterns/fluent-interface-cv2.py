class Css:
    
    def __init__(self):
        self.__s = ""
        self.__v = []
        self.__css = ""
    
    def selektor(self, name):
        self.__s = name
        return self
    
    def vlastnost(self, name):
        self.__v.append(name)
        return self
    
    def zobraz(self):
        self.__css = f"{self.__s} {{\n\t"
        self.__css += f"\n\t".join(self.__v)
        self.__css += f"\n{{"
        print(self.__css)
        return self
    
c = Css()
c.selektor("p").vlastnost("color: #CC0000;").vlastnost("text-decoration: none;").zobraz()