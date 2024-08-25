# Hash Table Collision Handling
class HashTable:
    def __init__(self):
        self.Max = 10
        self.arr = [[] for i in range(self.Max)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h = h + ord(char)
        return h % self.Max

    def __setitem__(self, key, value):  # this operator use to add key and value to the dictionary
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, value)
                found = True
                break
        if not found:
            self.arr[h].append((key, value))
        self.arr[h].append((key, value))
        print(f'{key} : {value} : {h}')

    def __getitem__(self, key):  # this operator sets key
        h = self.get_hash(key)
        print(self.arr[h])
        return self.arr[h]

    def __delitem__(self, key):  # this operator deletes key and value
        h = self.get_hash(key)
        self.arr[h] = None


if __name__ == '__main__':
    t = HashTable()
    t['july 64'] = 42
    t['aug 8'] = 13
    t['july 53'] = 43
    t['april 5'] = 142
    print(t.arr)
