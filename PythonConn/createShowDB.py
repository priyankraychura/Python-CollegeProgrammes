import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = ""
)

print("Connection object: ")
print(mydb)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE pvr")

print("Print list of databases: ")
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)