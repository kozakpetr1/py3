import sys

fname = "C:\\Users\petr.kozak\Documents\VSCodeProjects\py3\Files\SomeFile.txt"
try:
    foo = open(fname, 'rt', encoding="utf-8")
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    sys.exit()
except: #handle other exceptions such as attribute errors
    print ("Unexpected error:", sys.exc_info()[0])
with foo:
    print(foo.read())