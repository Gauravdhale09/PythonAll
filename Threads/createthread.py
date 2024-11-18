from threading import *

def display():
    print("Hello i am running")

for i in range(5):
    t = Thread(target=display)
    t.start()