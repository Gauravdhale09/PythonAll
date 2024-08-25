import mysql.connector as c
connect = c.connect(host='localhost',username='root',password='GRD@mysql09')

cursor = connect.cursor()
database_name = "Database1"
cursor.execute(f"CREATE DATABASE if not exists {database_name}")
print("Database created successfully")
insert_query = "INSERT INTO my_table (data) VALUES (%s)"
