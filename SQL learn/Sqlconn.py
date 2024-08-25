import mysql.connector as c

connect = c.connect(host='localhost',username='root',password='GRD@mysql09',database='JsonDatabase')

cursor = connect.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS grd")

table1_dict = "id varchar(20), name varchar(20), age integer(3)"
cursor.execute(f"CREATE TABLE IF NOT EXISTS Table1({table1_dict})")

connect.commit()
connect.close()