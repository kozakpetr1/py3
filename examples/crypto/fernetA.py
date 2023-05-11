import sys
import os.path
from colorama import Fore, Back, Style
from cryptography.fernet import Fernet

class crpt():

    def __init__(self, argv: tuple) -> None:
        if (len(argv) == 4):
            self.__what_to_do = argv[1]
            self.__file = argv[2]
            self.__data = None
            self.__key_file = argv[3]
            self.__key = Fernet.generate_key()
            self.__fernet = None
        else:
            raise Exception("Sorry, arguments do not match.")
    
    def check_key_file(self) -> bool:
        """Checkuj soubor s klíčem a načti klíč do __key

        Returns:
            bool: Vrací dycky True (Dycky Most!)
        """
        if (os.path.isfile(self.__key_file) and os.path.getsize(self.__key_file) > 0):
            foo = open(self.__key_file, "rb")
            self.__key = foo.read()
            foo.close()
        return True
            
    def check_file(self) -> bool:
        """Checkuj soubor pro šifrování a načti obsah do __data

        Returns:
            bool: ¨Vrací true, když do __data načteno
        """
        if (os.path.isfile(self.__file) and os.path.getsize(self.__file) > 0):
            foo = open(self.__file, "rb")
            self.__data = foo.read()
            foo.close()
            return True
        else:
            return False
    
    def check_cmd(self) -> bool:
        """Checkuj, jestli má atribut __shat_to_do hodnotu -e (encrypt) nebo -d (decrypt)

        Returns:
            bool: Pokud jo, tak vrací True
        """
        return True if (self.__what_to_do in ("-d", "-e")) else False
    
    def __str__(self) -> str:
        return f"{self.__what_to_do} {self.__file} {self.__key_file}"
    
    def check(self) -> bool:
        """Checkuj vstupní argumenty příkazového řádku

        Returns:
            bool: Vrací True, když jsou argumenty OK
        """
        return True if (self.check_key_file() and self.check_file() and self.check_cmd()) else False

    def crypto(self) -> bool:
        """Šifruj bo dešifruj fajl __file

        Returns:
            bool: Vrací True, když je šifruňk nabo dešifruňk OK
        """
        self.__fernet = Fernet(self.__key)
        if (self.__what_to_do == '-e'):
            print(Fore.BLACK + Back.CYAN + 'Provádím šifruňk ' + self.__file, end = '')
            print(Style.RESET_ALL)
            print
            token = self.__fernet.encrypt(self.__data)
            foo = open(self.__file + ".cry", 'wb')
            foo.write(token)
            foo.close()
            key = open(self.__key_file, 'wb')
            key.write(self.__key)
            key.close()
            os.remove(self.__file)
            return True
        elif (self.__what_to_do == '-d'):
            print(Fore.BLACK + Back.CYAN + 'Provádím dešifruňk ' + self.__file + " do " + self.__file[0:-3], end = '')
            print(Style.RESET_ALL)
            print
            token = self.__fernet.decrypt(self.__data)
            foo = open(self.__file[0:-3], 'wb')
            foo.write(token)
            foo.close()
            os.remove(self.__file) 
            os.remove(self.__key_file) 
            return True
        else:
            return False
    
c = crpt(sys.argv)
if (c.check()):
    c.crypto()
