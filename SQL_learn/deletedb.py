import mysql.connector as c
connect = c.connect(host='localhost',username='root',password='GRD@mysql09')

cursor = connect.cursor()
database_name = "Database1"
cursor.execute(f"DROP DATABASE if exists {database_name}")
print("Database deleted successfully")