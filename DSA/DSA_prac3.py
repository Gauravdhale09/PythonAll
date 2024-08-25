#Hash Table
# print(ord('m'))
# print(ord('a'))  # ord finds ascii value of the character
# print(ord('d'))

# def get_hash_table(key): # key is a string
#     h = 0
#     for char in key:
#         h = h + ord(char)
        
#         print(h)
#     print(h % 100)   #let assume 100 is a size of list
# get_hash_table('march 6')

class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [None for i in range(self.Max)]
        
        
    def get_hash(self,key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.Max
        
    def __setitem__(self,key,value): #this operator use to add key and value to the dictionary
        h = self.get_hash(key)
        self.arr[h] = value
        print(f'{key} : {value} : {h}')
    def __getitem__(self,key):  #this operator sets key

        h = self.get_hash(key)
        return self.arr[h]
    def __delitem__(self,key): #this operator deletes key and value    
        h = self.get_hash(key)
        self.arr[h] = None

if __name__ == '__main__':
    t = HashTable()
    t['june 26'] = 345
    t['march 6'] = 130
    t['june 9'] = 123
    t['may 6'] = 420
    t['july 64'] = 42
    t['aug 8'] = 13
    t['july 53'] = 43
    t['april 5'] = 142
    print(t.arr)

