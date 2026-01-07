class Teacher:
    
    def __init__(self, fname, lname, nick, age, status, grade):
        self.fname = fname
        self.lname = lname
        self.nick = nick
        self.age = age
        self.status = status
        self.grade = grade
    
    def getInfo(self):
        return str(self.fname) + " " + str(self.lname) + ", " + str(self.grade)
    
sbor = {
    "kozina" : Teacher("Petr", "Kozák", "kozy", 52, "married", 3),
    "herman" : Teacher("Petr", "Heřmanský", "berta", 60, "angry", 2),
    "cyril" : Teacher("Cyril", "Kochrda", "cinko", 52, "active", 2)
}

# print(sbor["herman"].getInfo())

for x in sbor.values():
  print(x.getInfo())
