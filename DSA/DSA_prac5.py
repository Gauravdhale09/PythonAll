# # Stack Data Structure
#
# s = []
# s.append("E1")
# s.append("E2")
# s.append("E3")
# s.append("E4")
# s.append("E5")
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# s.pop()
# print(s)

from collections import deque

# stack = deque()
# stack.append('E1')
# stack.append('E2')
# stack.append('E3')
# stack.append('E4')
# stack.append('E5')
# print(stack)
# stack.pop()
# print(stack)

class Stack:
    def __init__(self):
        self.contain = deque()
    def push(self,val):
        self.contain.append(val) #adds new element element
    def pop(self):
       return self.contain.pop() #removes top element
    def peek(self):
        return self.contain[-1] #prints top element
    def is_empty(self):
        print(len(self.contain) == 0)
        return len(self.contain)==0 #check whether stack is empty or not
    def size(self):
        print(len(self.contain))
        return len(self.contain) #size
    def rev(self):
        self.contain.reverse()
        print(self.contain)
if __name__ == '__main__':
    s = Stack()
    s.push(45)
    s.push(46)
    s.push(42)
    s.push(47)
    s.push(47)
    s.push(47)
    print(s)
    print(s.contain)
    s.is_empty()
    s.size()
    s.rev()

