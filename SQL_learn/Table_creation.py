import mysql.connector as c

connect = c.connect(host='localhost',username='root',password='GRD@mysql09', database= 'Database1')
if connect.is_connected():
    print('Connected to MySQL database')
cursor = connect.cursor()

table1_dict = "id varchar(20), name varchar(20), age integer(3)"
cursor.execute(f"CREATE TABLE IF NOT EXISTS Table1({table1_dict})")
print("Table created successfully")
variables = ('id', 'name', 'age')
char = ()
q1 = f"INSERT INTO Table1{variables} VALUES(%s, %s, %s)"
v1 = (('1', 'John', 30), ('2', 'Johncena', 30), ('3', 'Johnmaina', 30))
for i in v1:
    cursor.execute(q1, i)
connect.commit()
connect.close()
print("Table created successfully")
