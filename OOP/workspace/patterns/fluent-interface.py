class Texto:
    
    def __init__(self, *argv):
        self.__t = list(argv)
        self.__s = ""
        
    def getList(self):
        return self.__t

    def getText(self):
        return self.__s
        
    def addText(self, t):
        self.__t.append(t)
        return self
        
    def removeText(self, t):
        self.__t.remove(t)
        return self
        
    def popText(self, index):
        self.__t.pop(index)
        return self

    def concatText(self, spojka = " "):
        self.__s = spojka.join(self.__t)
        return self

t = Texto("Přelet", "nad", "kukaččím", "hnízdem")
# fluentní interface
t.addText(".").concatText().removeText(".").removeText("hnízdem").addText("hnízdem.").concatText()
print(t.getText())
