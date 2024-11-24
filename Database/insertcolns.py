import mysql.connector as c
from mysql.connector import errorcode

try:
    conn = c.connect(
        host="localhost",
        user="root",
        database="Students",
    )
    cursor = conn.cursor()

    add_columns_query = """
    ALTER TABLE catlog
    ADD COLUMN father_name VARCHAR(255) NOT NULL,
    ADD COLUMN mother_name VARCHAR(255) NOT NULL
    """

    cursor.execute(add_columns_query)
    print("Columns added successfully.")

except c.Error as e:
    print("Error", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")