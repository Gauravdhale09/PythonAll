class Human:
    def __init__(self, first, last):
        self.fname = first
        self.lname = last  # this are properties (first name and last name) of class

    def id(self, number):
        print(number, " is the id of ", self.fname)

    def work(self, profession):
        print(profession, " is the work of ", self.fname)    #This are the methods of class Human


if __name__ == '__main__':
    hun = Human("rayan", "yadav")
    print(hun.fname)
    hun.work("player")
    hun.id(778)

