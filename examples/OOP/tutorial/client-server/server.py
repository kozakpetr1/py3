import socket
import random as r
import re
import os
from pathlib import Path

class Server:
    
    mood = ['I am OK.', 'Angry!', 'Bad mood!', 'Good mood!', 'Do not send me this kind of questions!']
    hobbies = ['Communication', 'Programming', 'Trolling', 'Hacking', 'Crashing', 'Lying']
    name = ['Brutus', 'Thanos', 'Longinus', 'Xavier', 'Sasa', 'Obama', 'Trump', 'Biden']

    def __init__(self, **kwargs):

        self.__host = kwargs['host'] if 'host' in kwargs else socket.gethostname()
        self.__port = kwargs['port'] if 'port' in kwargs else 5000

        self.__server_socket = socket.socket()  # get instance
        self.__server_socket.bind((self.__host, self.__port))
        
        self.__ascii = {}
 
        for p in Path(f"{os.path.dirname(os.path.realpath(__file__))}\\cmds\\").glob('*'):
            with p.open() as f:
                self.__ascii[f"{p.name}"] = f.read()
        
    def compile(self):
            
        if re.search("^=.*$", self.__recieved_data):
            return str(eval(self.__recieved_data[1:]))
        else:
            match(self.__recieved_data):
            
                case 'Hi!': return 'Hello!'
                case '#rand': return str(r.randint(1, 1000))
                case '#finger': return self.__ascii['finger']
                case '#clown': return self.__ascii['clown']
                case '#clear':
                    os.system('cls')
                    return 'Server clearscreen finished.'
                case '#cwd': return os.getcwd()        
                case 'Your mood?': return Server.mood[r.randint(0, len(Server.mood) - 1)]
                case 'Your hobbies?': return Server.hobbies[r.randint(0, len(Server.hobbies) - 1)]
                case 'Your name?': return Server.name[r.randint(0, len(Server.name) - 1)]
                case _ : return None

    def listen(self):
        print(f"Listening on {self.__host}:{self.__port}")
        self.__server_socket.listen(2)
        self.__conn, self.__address = self.__server_socket.accept()
        print("<- " + str(self.__address))

        while True:
            self.__recieved_data = self.__conn.recv(1024).decode()
            if not self.__recieved_data:
                break
            print("<- " + str(self.__recieved_data))
            self.__data = self.compile()
            if self.__data == None:
                self.__data = input(' $ ')
            self.__conn.send(self.__data.encode())
                
        self.__conn.close()

if __name__ == '__main__':
    server = Server()
    server.listen()
