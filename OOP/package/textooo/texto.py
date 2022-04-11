class Texto:
    """
    """

    def __init__(self, str):
        self.str = str
    
    def getS(self):
        return self.str
    
    def replaS(self, what, byWhat, str = None):
        if not str == None: self.str = str
        self.str = self.str.replace(what, byWhat)
        