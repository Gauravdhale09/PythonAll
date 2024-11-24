
import mysql.connector as c
from mysql.connector import errorcode

try:
    conn = c.connect(
        host="localhost",
        user="root",
        database="Students",
    )

    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS catlog (
        id INT PRIMARY KEY,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL,
        Date_of_birth VARCHAR(8) NOT NULL,
        gender VARCHAR(255) NOT NULL,
        admission_year INT NOT NULL,
        created_at TIMESTAMP NOT NULL
    )
    """
    cursor.execute(create_table_query)
    print("Table created successfully.")

except c.Error as e:
    print("Error: %s" % e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
    