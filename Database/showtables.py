import mysql.connector as c
from mysql.connector import errorcode

try:
    conn = c.connect(
        host="localhost",
        user="root",
        database="Students",
    )

    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")
    print("Tables in the Students database:")

    for table in cursor:
        print(table[0])

except c.Error as e:
    print("Error: %s" % e)
finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")

    