class Book:
    
    def __init__(self, name, author, num):
        self.name = name
        self.author = author
        self.num_of_pages = num
        
    def about(self):
        return self.name + " writen by " + self.author + ", " + str(self.num_of_pages) + " pages."
    
    def read(self, reader):
        return reader + " reads " + self.name + "."

b1 = Book("Egypťan Sinuhet", "Mika Waltari", 830)
print(b1.about())
print(b1.read("Matěj Stebel"))

b2 = Book("Výherní vkladní knížka", "Česká spořitelna", 20)
print(b2.about())
print(b2.read("Jakub Svoboda"))
