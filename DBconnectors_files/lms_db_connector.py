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
    def validateUser(self,username,password):
        row = (username, password)
        query = "SELECT * FROM `user` WHERE username=%s AND password=%s"
        cursor.execute(query,row)
        records = cursor.fetchall()
        print(cursor.rowcount)
        if cursor.rowcount==1:
            print("Login successfully")
            return  1
        else:
            print("Login Failed")
            return 0
"""obj=librarydbconnection()
obj.makeconnection()
Uname = input("Enter username")
Pass = input("Enter password")
obj.validateUser(Uname,Pass)"""

