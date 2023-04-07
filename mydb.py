#Install mysql
#pip install mysql
#pip install mysql-conector
#pip install mysql-connector-python

import mysql.connector

database = mysql.connector.connect(
    host= 'localhost',
    user = 'root',
    passwd = 'root'

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("DONE!!!!")