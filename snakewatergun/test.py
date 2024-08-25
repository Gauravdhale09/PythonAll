import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client['sample']
col = database['sample1']
z = input("Enter 3 integer object id")
x  = input("Enter email=")
y = input("Enter 6 digit password")
if ("@gmail.com" in x) and (len(y) == 6) and (len(z)==3):
    try:
        dict1 = {"_id":z, "email:": x, "password:": y}
        col.insert_one(dict1)
    except Exception as e:
        print(e)
else:
    print("invalid credentials")