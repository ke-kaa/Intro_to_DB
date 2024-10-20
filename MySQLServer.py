import mysql.connector
from mysql.connector import Error

host = 'localhost'
user = 'root'
password = 'password'

try:
    connection = mysql.connector.connect(
        host=host, 
        user=user,
        password=password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        cursor.execute("CREATE DADTABSE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()