import sys
import os.path
from colorama import Fore, Back, Style
from cryptography.fernet import Fernet

if (len(sys.argv) == 4):
    s = { "__what_to_do" : sys.argv[1],
        "__file" : sys.argv[2],
        "__data" : None,
        "__key_file" : sys.argv[3],
        "__key" : Fernet.generate_key(),
        "__fernet" : None
    }
else:
    raise Exception("Sorry, arguments do not match.")
    
def check_key_file() -> bool:
    """Checkuj soubor s klíčem a načti klíč do __key

    Returns:
        bool: Vrací dycky True (Dycky Most!)
    """
    if (os.path.isfile(s["__key_file"]) and os.path.getsize(s["__key_file"]) > 0):
        foo = open(s["__key_file"], "rb")
        s["__key"] = foo.read()
        foo.close()
    return True
            
def check_file() -> bool:
    """Checkuj soubor pro šifrování a načti obsah do __data

    Returns:
        bool: ¨Vrací true, když do __data načteno
    """
    if (os.path.isfile(s["__file"]) and os.path.getsize(s["__file"]) > 0):
        foo = open(s["__file"], "rb")
        s["__data"] = foo.read()
        foo.close()
        return True
    else:
        return False

def check_cmd() -> bool:
    """Checkuj, jestli má atribut __shat_to_do hodnotu -e (encrypt) nebo -d (decrypt)

    Returns:
        bool: Pokud jo, tak vrací True
    """
    return True if (s["__what_to_do"] in ("-d", "-e")) else False
    
def check() -> bool:
    """Checkuj vstupní argumenty příkazového řádku

    Returns:
        bool: Vrací True, když jsou argumenty OK
    """
    return True if (check_key_file() and check_file() and check_cmd()) else False
    
def crypto() -> bool:
    """Šifruj bo dešifruj fajl __file

    Returns:
        bool: Vrací True, když je šifruňk nabo dešifruňk OK
    """
    s["__fernet"] = Fernet(s["__key"])
    if (s["__what_to_do"] == '-e'):
        print(Fore.BLACK + Back.CYAN + 'Provádím šifruňk ' + s["__file"], end = '')
        print(Style.RESET_ALL)
        print
        token = s["__fernet"].encrypt(s["__data"])
        foo = open(s["__file"] + ".cry", 'wb')
        foo.write(token)
        foo.close()
        key = open(s["__key_file"], 'wb')
        key.write(s["__key"])
        key.close()
        os.remove(s["__file"])
        return True
    elif (s["__what_to_do"] == '-d'):
        print(Fore.BLACK + Back.CYAN + 'Provádím dešifruňk ' + s["__file"] + " do " + s["__file"][0:-3], end = '')
        print(Style.RESET_ALL)
        print
        token = s["__fernet"].decrypt(s["__data"])
        foo = open(s["__file"][0:-3], 'wb')
        foo.write(token)
        foo.close()
        os.remove(s["__file"]) 
        os.remove(s["__key_file"]) 
        return True
    else:
        return False
    
if (check()):
    crypto()
