import socket
import sys
import os
from time import sleep
import random as r


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Client:
    
    def __init__(self, **kwargs):
        
        self.__host = kwargs['host'] if 'host' in kwargs else socket.gethostname()
        self.__port = kwargs['port'] if 'port' in kwargs else 5000
       
        self.__client_socket = socket.socket()
        self.__client_socket.connect((self.__host, self.__port))  


    def go(self):
        
        os.system('cls')
        r.seed()
        self.__message = input(" $ ") 
        
        while self.__message.lower().strip() != 'bye':
            self.__client_socket.send(self.__message.encode())
            self.__data = self.__client_socket.recv(1024).decode()
            print(f"-> {bcolors.OKBLUE}", end ="")
            for char in self.__data:
                sleep(r.random() * 0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            print(f"{bcolors.ENDC}")
            self.__message = input(" $ ")

        self.__client_socket.close()
        
if __name__ == '__main__':
    client = Client()
    client.go()
