import pymongo as po
#connect to mongodb
client=po.MongoClient('mongodb://localhost:27017')
#create database(base and collection name is must)
database = client['Signup']
coll = database['ok']
x=input("Enter gmail=")
y = input("Enter password=")
list1 = [{"Name":x,"password":y},

         {"intake":270,"end":2024}]
coll.insert_many(list1)

