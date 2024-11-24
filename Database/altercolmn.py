import mysql.connector as c
from mysql.connector import errorcode

def alter_column():
    conn = c.connect(
        host="localhost",
        user="root",
        database="Students",
    )

    cursor = conn.cursor()

    alter_query = "ALTER TABLE catlog MODIFY COLUMN Date_of_birth VARCHAR(20);"

    cursor.execute(alter_query)

    print("Column modified successfully.")

alter_column()