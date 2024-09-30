import mysql.connector as db
from mysql.connector import Error

class MyComics:
    
    def __init__(self, **kwargs):
        self.__host = str(kwargs["host"]) if "host" in kwargs.keys() else "localhost"
        self.__db = str(kwargs["db"]) if "db" in kwargs.keys() else "comics"
        self.__user = str(kwargs["user"]) if "user" in kwargs.keys() else "root"
        self.__psswd = str(kwargs["psswd"]) if "psswd" in kwargs.keys() else ""
        self.__connection = None
        self.__cursor = None
        self.__row = None
        self.__data = list()
        self.__query = ""
        self.__studios = list()
        self.__characts = list()
        print ("*"*20 + " Komiksové postavy " + "*"*20)
        
    def connect(self) -> int:
        try:
            self.__connection = db.connect(host = self.__host, database = self.__db, user = self.__user, password = self.__psswd)
            if self.__connection.is_connected():
                self.__cursor = self.__connection.cursor(dictionary = True, buffered = True)
                self.__cursor.execute("select database();")
                self.__cursor.fetchone()
        except Error as e:
            print("Error while connecting to MySQL", e)
            return False
        return True
    
    def closeConnection(self):
        if self.__connection.is_connected():
            self.__cursor.close()
            self.__connection.close()
            
    def execQuery(self, query):
        self.__query = query
        try:
            self.__cursor.execute(self.__query)
        except Error as e:
            print("Error while executing query", e)
            print(self.__query)
            return False
        self.__connection.commit()
        return True

    def getData(self):
        self.__data.clear()
        self.__row = self.__cursor.fetchone()
        while self.__row is not None:
            self.__data.append(self.__row)
            self.__row = self.__cursor.fetchone()
        return self.__data
    
    def insertNewCharacter(self):
        print("|--- Nová postava")
        name = str(input("Jméno postavy: "))
        weapon = str(input("Zbraně: "))
        studio = int(input("Číslo studia: "))
        ins = False
        for l in self.__studios:
            if studio == l["id"]:
                ins = True
        if ins:
            return self.execQuery("INSERT INTO charact(id, name, weapon, studio_id) VALUES(NULL, '{}', '{}', {});".format(name, weapon, studio))
        else:
            return False

    def getStudios(self):
        self.__studios.clear()
        if self.execQuery("SELECT * FROM studio"):
            self.__studios = self.getData()
            for st in self.__studios:
                print("Studio: {}. {}".format(st["id"], st["name"]))
            return True
        else:
            return False

    def getCharacts(self):
        self.__characts.clear()
        if self.execQuery("SELECT charact.id, charact.name, charact.weapon, studio.name AS sname FROM charact JOIN studio WHERE charact.studio_id = studio.id ORDER BY charact.id DESC LIMIT 1;"):
            print("|--- Poslední přidaná postava")
            self.__characts = self.getData()
            for c in self.__characts:
                print("Jméno postavy: %s" % c["name"], "zbraně: %s" % c["weapon"], "studio: %s" % c["sname"], sep = "\n")
            return True
        else:
            return False

    def __del__(self):
        self.closeConnection()

if __name__ == "__main__":
    comics = MyComics()
    if comics.connect():
        if comics.getStudios():
            if comics.insertNewCharacter():
                print("|--- Přidána nová postava.")
            else:
                print("|--- Novou postavu nebylo možné přidat.")
            comics.getCharacts()
    del comics
