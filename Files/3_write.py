import sys

fname = "C:\\Users\petr.kozak\Documents\VSCodeProjects\py3\Files\SomeFile.txt"
textToAppend = "Toto je připojený text k souboru."

try:
    foo = open(fname, 'at', encoding="utf-8")
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    sys.exit()
except: #handle other exceptions such as attribute errors
    print ("Unexpected error:", sys.exc_info()[0])
    sys.exit()

try:
    foo.writelines(textToAppend)
except IOError as e:
    print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    sys.exit()
except: #handle other exceptions such as attribute errors
    print ("Unexpected error:", sys.exc_info()[0])
    sys.exit()

foo.close()