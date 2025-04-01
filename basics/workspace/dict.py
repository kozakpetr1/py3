person = {
    "firstname" : "Klaudius",
    "lastname"  : "Picmaus",
    "hobbies"   : ["soccer", "therian", "parkur"],
    "sex"       : "Male",
    "year"      : 2000
}

class Catalogue:
    
    def __init__(self):
        self.__people = []
        
    def addItem(self, item):
        if isinstance(item, dict):
            self.__people.append(item)
        
    def showMe(self):
        print(self.__people)
        
p = Catalogue()
p.addItem(person)
p.addItem({"firstname:" : "Jan", "lastname" : "z Vysočan"})
p.addItem(12354835)
p.addItem(["Jan", "z Vysočan"])
p.showMe()