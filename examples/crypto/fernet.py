import sys
import os.path
from colorama import Fore, Back, Style
from cryptography import Fernet

class param_checker():

    def __init__(self, argv: tuple) -> None:
        if (len(argv) == 4):
            self.__what_to_do = argv[1]
            self.__file = argv[2]
            self.__key_file = argv[3]
            self.__key = None
        else:
            raise Exception("Sorry, arguments do not match.")
    
    def is_key_file(self) -> bool:
        return True if (os.path.isfile(self.__key_file)) else False
            
    def is_file(self) -> bool:
        return True if (os.path.isfile(self.__file)) else False
    
    def is_cmd(self) -> bool:
        return True if (self.__what_to_do in ("-d", "-e")) else False
    
    def __str__(self) -> str:
        return f"{self.__what_to_do} {self.__file} {self.__key_file}"
    
    def check(self):
        return True if (self.is_key_file() and self.is_file() and self.is_cmd()) else False
    
    
    
checker = param_checker(sys.argv)
print(checker)
print(checker.check())
