import mysql.connector as c

connect = c.connect(host='localhost',username='root')

cursor = connect.cursor()
cursor.execute("CREATE database IF NOT EXISTS JsonDatabase")  # create database


print("database JsonDatabase created successfully")

connect2 = c.connect(host='localhost',username='root', database='JsonDatabase')

cursor2 = connect2.cursor()

table1_dict = "id varchar(20), name varchar(20), age integer(3)"
cursor2.execute(f"CREATE TABLE IF NOT EXISTS Table1({table1_dict})")  # create table

q1 = "INSERT INTO Table1(id, name, age) VALUES(%s, %s, %s)"
d1 = ("233212", "Gaurav", 21)
cursor2.execute(q1,d1)
connect2.commit()
cursor2.execute("SELECT @@datadir")
data_dir = cursor2.fetchone()

print(f"MySQL data directory: {data_dir[0]}")
cursor.close()         #close connection
