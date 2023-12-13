import socket
import sys
from time import sleep
import random as r


class Client:
    
    def __init__(self, **kwargs):
        
        self.__host = kwargs['host'] if 'host' in kwargs else socket.gethostname()
        self.__port = kwargs['port'] if 'port' in kwargs else 5000
       
        self.__client_socket = socket.socket()
        self.__client_socket.connect((self.__host, self.__port))  

    def go(self):
        
        r.seed()
        self.__message = input(" $ ") 
        
        while self.__message.lower().strip() != 'bye':
            self.__client_socket.send(self.__message.encode())
            self.__data = self.__client_socket.recv(1024).decode()
            print('-> ', end ="")
            for char in self.__data:
                sleep(r.random() * 0.25)
                sys.stdout.write(char)
                sys.stdout.flush()
            print("")
            self.__message = input(" $ ")

        self.__client_socket.close()
        
if __name__ == '__main__':
    client = Client(ost = "192.168.56.1", port=50000)
    client.go()
