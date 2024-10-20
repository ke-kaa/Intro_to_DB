import mysql.connector

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

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except except mysql.connector.Error as e:
    print(f"Error: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
