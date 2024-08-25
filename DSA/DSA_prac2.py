#Linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(Node):
    def __init__(self):
        self.head = None

    def insert_at_begin(self,data):
        self.head = Node(data, self.head)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count                 
    def print(self):
        if self.head is None:
            print("list is empty")
            return

        itr = self.head
        print(itr)
        listr = ''
        while itr:
            listr = listr + str(itr.data) + '-->'
            itr = itr.next
            print(itr)
        print(listr)    
    def remove(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Index out of range")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr  = itr.next    
            count += 1
    def insert(self, index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Index out of range")   
        if index == 0:
            self.insert_at_begin(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    
    ll.insert_values([123,64,649,74])
    ll.insert_at_begin(66)
    print("length:",ll.get_length())
    
    ll.print()