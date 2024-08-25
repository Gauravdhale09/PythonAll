import mysql.connector as c

connect = c.connect(host='localhost',username='root',password='GRD@mysql09')

cursor = connect.cursor()
cursor.execute("CREATE database IF NOT EXISTS JsonDatabase")  # create database
cursor.execute("DROP database IF EXISTS JsonDatabase")     # delete database


print("database JsonDatabase created successfully")

connect2 = c.connect(host='localhost',username='root',password='GRD@mysql09', database= 'JsonDatabase')

cursor2 = connect2.cursor()

table1_dict = "id varchar(20), name varchar(20), age integer(3)"
cursor2.execute(f"CREATE TABLE IF NOT EXISTS Table1({table1_dict})")  # create table

q1 = "INSERT INTO Table1(id, name, age) VALUES(%s, %s, %s)"
d1 = ("233212", "Gaurav", 21)
cursor2.execute(q1,d1)
connect2.commit()
cursor.close()         #close connection
