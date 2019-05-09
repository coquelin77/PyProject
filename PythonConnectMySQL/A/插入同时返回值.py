import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="zym163453",
    database="runoob_db"
)
mycursor = mydb.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("Zhihu", "https://www.zhihu.com")
mycursor.execute(sql, val)

mydb.commit()

print("1 条记录已插入, ID:", mycursor.lastrowid)