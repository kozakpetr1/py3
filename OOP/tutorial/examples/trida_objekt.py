class Human:

    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def set_name(self, new_fname, new_lname):
        self.first_name = new_fname
        self.last_name = new_lname

it2 = [
    Human("Rostislav", "Patočka"),
    Human("Jakub", "Pikal"),
    Human("Matěj", "Jankech"),
    Human("Marin", "Prodan")
]

for i in it2:
    print(i)