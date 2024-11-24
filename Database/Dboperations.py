import mysql.connector as c
from mysql.connector import errorcode
from datetime import datetime
# query = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * (len(datalist)-1))}, NOW())"
# self.cursor.execute(query, datalist)
# self.conn.commit()
class DbOperations:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = c.connect(
            host="localhost",
            user="root",
            database=self.db_name
        )

        self.cursor = self.conn.cursor()
        print(f"Connected to {self.db_name} database.")

    def create_id(self, dob, ayear):
        doblst = str(dob).split('/')
        print(doblst)
        dob = f"{doblst[0]}{doblst[1]}{doblst[2][2:]}" 
        student_id = f"{dob}{str(ayear)[2:]}"
        return student_id

    def list_columns(self, table_name):
        query = f"DESCRIBE {table_name}"
        self.cursor.execute(query)
        for column in self.cursor.fetchall():
            print(f"Column {column[0]}, type: {column[1]}")

    def insert_data(self, table_name, datadict):
        query = f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(list(datadict.values())))})"
        self.cursor.execute(query, list(datadict.values()))
        self.conn.commit()
        print(f"{self.cursor.rowcount} record inserted.")

    def delete_row(self, table, stid):
        query = f"DELETE FROM {table} WHERE id = %s"
        self.cursor.execute(query, (stid,))
        self.conn.commit()
        print(f"{self.cursor.rowcount} record deleted.")

    def retrieve_allrows(self, table_name):
        query = f"SELECT * FROM {table_name}"
        self.cursor.execute(query)
        rows= self.cursor.fetchall()
        print(f"Total rows retrieved {self.cursor.rowcount}")
        for row in rows:
            print(row)

if __name__ == "__main__":
    try:
        name = "Students"
        
        # dict = {"name":"Ratj"}
        # print(list(dict.values()))
        db = DbOperations(name)
        firstnames = ["Aarav",
        "Vivaan",
        "Ishita",
        "Ananya",
        "Rohan",
        "Sneha",
        "Kavya",
        "Aditya",
        "Priya",
        "Rajesh"]
        lastnames = ["Patil",
        "Paraskar",
        "Maanekar",
        "Tibdewal",
        "Shah",
        "Shivam",
        "Rajat",
        "Raghu",
        "Raghav",
        "Raghunath"]
        dobs = [
        "12/09/2002",
        "05/03/1998",
        "23/07/2000",
        "15/11/2001",
        "30/04/1999",
        "18/06/2003",
        "09/12/2004",
        "25/08/2000",
        "01/01/1997",
        "14/10/2002"]
        genders = [
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female",
        "Male",
        "Female"]
        adyears = [
        2015,
        2016,
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024]
        fathernames = [
        "Ramesh",
        "Suresh",
        "Mahesh",
        "Rajesh",
        "Vikram",
        "Prakash",
        "Harish",
        "Anil",
        "Kishore",
        "Sanjay"]
        mothernames = [
        "Sunita",
        "Kavita",
        "Meena",
        "Anjali",
        "Geeta",
        "Lakshmi",
        "Pooja",
        "Shalini",
        "Priya",
        "Saraswati"]

        for fn, ln, dob, gr, ay, ftn, mtn in zip(firstnames, lastnames, dobs, genders, adyears, fathernames, mothernames):
            stid = db.create_id(dob, ay)
            data = {
                "id":stid,
                "first_name": fn,
                "last_name": ln,
                "Date_of_birth": dob,
                "gender": gr,
                "admission_year": ay,
                "created_at": datetime.now(),
                "father_name": ftn,
                "mother_name": mtn
            }
            db.insert_data("catlog", data)
            print(f"Inserted data for {fn} {ln}.")
        # db.list_columns("catlog")
        # db.insert_data("catlog", data)
        # db.retrieve_allrows("catlog")
        db.delete_row("catlog", 9120421)

    except c.Error as e:
        if e.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"The database {name} does not exist.")
        else:
            print(f"The error '{e}' occurred")

