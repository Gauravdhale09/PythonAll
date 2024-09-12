import pymongo as po
client=po.MongoClient('mongodb://localhost:27017')
database = client['Signup']
schema = database['ok']
x=input("Enter gmail=")
y = input("Enter password=")
list1 = [{"Name":x,"password":y},

         {"intake":270,"end":2024}]
schema.insert_many(list1)

