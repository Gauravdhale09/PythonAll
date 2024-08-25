# q = []
# q.insert(0,42)
# q.insert(4,46)
# q.insert(7,44)
# q.pop()
# print(q)

from collections import deque
# q = deque()
# q.appendleft(54)
# q.appendleft(534)
# q.appendleft(554)
# q.appendleft(56)
# q.pop()
# print(q)

class Queue:
    def __init__(self):
        self.que = deque()
    def enq(self,val):  # for inserting items from left
        self.que.appendleft(val)
    def deque(self):
        self.que.pop()
    def size(self):
        return len(self.que)
if __name__ == '__main__':
    q = Queue()
    q.enq(46)
    q.enq(45)
    q.enq(458)
    print(q.que)
    q.deque()
    print(q.que)