import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Jrepsa.9910'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE CRM")

print("ALL DONE!")