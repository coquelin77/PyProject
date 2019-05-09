import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="zym163453",
    database="runoob_db"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")