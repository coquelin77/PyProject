import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="zym163453",
    database="runoob_db"
)
mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)