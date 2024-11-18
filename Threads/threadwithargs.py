from threading import *

def display(strng):
    print(strng)

for i in range(5):
    t = Thread(target=display, args=('Hello', ))
    t.start()