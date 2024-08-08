import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "pvr"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers(rno INT(3), name VARCHAR(255), class VARCHAR(10), college VARCHAR(50))")

print("List of tables: ")
mycursor.execute("SHOW TABLES")
for i in mycursor:
    print(i)