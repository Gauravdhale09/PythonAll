from customtkinter import *

from tkinter import *

class Signup(Tk):
    def __init__(self, ):
        super(Signup, self).__init__()
        self.title("Signup")
        self.geometry("400x550")
if __name__ == '__main__':
    obj  = Signup()
    obj.mainloop()