import mysql.connector

# Connection details
host = 'localhost'
user = 'root'
password = 'barnista27'

# Connect to mondictionary_v2
conn1 = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='mondictionary_v2'
)
print("Connected to mondictionary_v2")

# Connect to TheMonLanguageDictionary
conn2 = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='TheMonLanguageDictionary'
)
print("Connected to TheMonLanguageDictionary")

# Don't forget to close connections when done
conn1.close()
conn2.close()