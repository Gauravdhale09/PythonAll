import mysql.connector as c

conn = c.connect(
    host="localhost",
    user="root",
)

cursor = conn.cursor()

cursor.execute("SHOW DATABASES")

print("databases in MySQL")
for db in cursor:
    print(db[0])

cursor.close()
conn.close()