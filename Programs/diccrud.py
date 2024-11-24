
class Crud:
    def __init__(self):
        self.dict = {}


    def create(self, key, value):
        self.dict[key] = value

    
    def update(self, key, value):
        if key in self.dict:
            self.dict[key] = value
        else:
            print("Key not found.")
    def delete(self, key):
        if key in self.dict:
            del self.dict[key]
        else:
            print("Key not found.")

    def retrieve(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            print("Key not found.")

if __name__ == "__main__":
    crud = Crud()
    crud.create("name", "John Doe")
    crud.create("age", 30)
    crud.create("city", "New York")
    crud.create("state", "America")

    print(crud.retrieve("name")) 
    # print(crud.retrieve("age"))
    # print(crud.retrieve("city")) 

    crud.update("age", 31)
    # print(crud.retrieve("age")) 
    crud.delete("city")
    print(crud.retrieve("city"))  
    print(crud.dict)

   
