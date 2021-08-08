# to works rename this file to database-connection.py and rename the variables: user, password, host and database to your machine configuration.

import mysql.connector

connection = mysql.connector.connect(user='youruser',password='yourpassword',host='yourhost',database='yourdatabase')

connection.close()
