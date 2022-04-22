import mysql.connector as db
from mysql.connector import Error

try:
    connection = db.connect(host='localhost', database='plang', user='root', password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        query = ("SELECT * FROM lang")
        cursor.execute(query)
        for (idlang, designation, created) in cursor:
            print("Language {} was created in {}.".format(designation, created))

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")