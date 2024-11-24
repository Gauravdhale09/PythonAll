import mysql.connector as c
from mysql.connector import errorcode

try:
    conn = c.connect(
        host="localhost",
        user="root",
    )

    cursor = conn.cursor()

    db_name = "Students"
    cursor.execute(f"CREATE DATABASE {db_name}")

    print(f"Database {db_name} created successfully.")

except c.Error as e:
    if e.errno == errorcode.ER_DB_CREATE_EXISTS:
        print("Database already exists.")
    else:
        print(f"The error '{e}' occurred")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")