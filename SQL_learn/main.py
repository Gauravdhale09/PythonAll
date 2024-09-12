import mysql.connector as c


class DatabaseOperations:
    def __init__(self):
        # first connect to your local host
        self.con = c.connect(host='localhost',username='root')
        self.cur = self.con.cursor()

    def create_new_database(self, database_name):
        # create database
        command_to_create_db = f"CREATE database IF NOT EXISTS {database_name}"
        self.cur.execute(command_to_create_db)
        self.con.commit()

        # make new connection with creted database

        self.con = c.connect(host='localhost',username='root', database=database_name)
        self.cur = self.con.cursor()
    
    def create_schema(self, schema_name, schema_dict):
        # create new schema with dict
        #e.g.
        #schema_name = table1
        #schema_dict = "id varchar(20), name varchar(20), age integer(3)"
        command_to_create_schema = f"CREATE TABLE IF NOT EXISTS {schema_name}({schema_dict})"
        self.cur.execute(command_to_create_schema)
        self.con.commit()


    def insert_data_into_schema(self, query, data):
        # insert data into schema
        #e.g.
        # QUERY : "INSERT INTO Table1(id, name, age) VALUES(%s, %s, %s)"
        # data : ("233212", "Gaurav", 21)
        self.cur.execute(query, data)
        self.con.commit()

    def check_the_path_of_db_saved(self):
        # check the path of the database saved
        self.cur.execute("SELECT @@datadir")
        data_dir = self.cur.fetchone()
        print(f"MySQL data directory: {data_dir[0]}")
    
    def delete_database(self, db_name):
        self.cur.execute(f"DROP DATABASE if exists {db_name}")
        print("Database deleted successfully")

if __name__ == "__main__":
    db_name = "db1"
    obj = DatabaseOperations()
    obj.create_new_database(db_name)
    obj.create_schema("table1", "id varchar(20), name varchar(20), age integer(3)")
    obj.insert_data_into_schema("INSERT INTO Table1(id, name, age) VALUES(%s, %s, %s)", ("233212", "Gaurav", 21))
    obj.check_the_path_of_db_saved()
    obj.delete_database("db1")