import mysql.connector
cursor= None
conn= None

class librarydbconnection:

    def makeconnection(self):
        global conn
        global cursor
        conn = mysql.connector.connect(user="root", password="", host="localhost", database="librarydb")
        if conn:
            print("connection sussessful")
            cursor = conn.cursor()
            print("cursor initialized")
            print(type(cursor))

        else:
            print("connection failed")
            exit(-1)
obj=librarydbconnection()
obj.makeconnection()


