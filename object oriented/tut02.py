class Vehicle:
    def usage(self):
        print("Use of vehicle is for general transportation")


class Car(Vehicle):
    def __init__(self):
        print("This is Car")
        self.wheels = 4
        self.roof = True
        self.door = True
    def work(self):
        print("For Family")
class Motor(Vehicle):
    def __init__(self):
        print("This is MO")
        self.wheels = 2
        self.roof = False
        self.door = False
    def work(self):
        print('For self')
c = Car()
c.usage()   
c.work()
m = Motor()
m.usage()         