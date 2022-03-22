""" File open
    Read file
    File close
"""

"""
    r - Read
    a - Append
    w - Write
    x - Create

    t - Text
    b - Binary
"""
# Otevření textového (t) souboru pro čtení (r) 
foo = open("C:\\Users\petr.kozak\Documents\VSCodeProjects\py3\Files\SomeFile.txt", "rt")

# načtení celého obsahu souboru metodou read()
print(foo.read())
foo.close()

foo = open("C:\\Users\petr.kozak\Documents\VSCodeProjects\py3\Files\SomeFile.txt", "rt")
# načtení jednoho řádku souboru metodou read()
print(foo.readline())
foo.close()

foo = open("C:\\Users\petr.kozak\Documents\VSCodeProjects\py3\Files\SomeFile.txt", "rt")
# čtení souboru po řádcích v loopu
for row in foo:
  print(row, end="")
foo.close()