import time

from customtkinter import *
from tkinter import *

import datetime
class Assist(CTk, Tk):
    def __init__(self):
        super(Assist, self).__init__()
        self.geometry("600x700+520+70")
        self.config(background="black")
        self.title("C-Assistant")


        def close():
            h = ""
            print(E_var.get())
            E_var.set(h)

        t_var = StringVar()

        E_var = StringVar()
        box = Entry(master=self,textvariable=E_var,font=("Raleway", 20, "bold"))
        E_var.set("Start writing....")
        box.place(x=20, y=500,height=300,width=710)
        CTkLabel(master=self,text="Mini Console",text_color='white',bg_color='black',font=("Raleway", 20)).place(x=16,y=396)
        lab = CTkEntry(master=self, textvariable=t_var, font=("Roboto", 20),text_color='black',bg_color='white',width=550)

        lab.place(x=25, y=450)
        button1 = CTkButton(master=self, text="Enter", font=("Raleway", 20),command=close)
        button1.place(x=200, y=50)


if __name__ == '__main__':
    mypass = "GRD@assistant"
    root = CTk()
    root.title("ConfirmIdentity")
    root.geometry("1200x500+250+200")

    def confirm():
        Label(master=root, text="Confirming identity...", font=("Roboto", 20)).place(x=490, y=80)
        if p_ver.get() == mypass:
            Label(master=root, text="Identity Confirmed", font=("Roboto", 20)).place(x=490, y=130)
            now = datetime.datetime.now().time()
            if 12 > now.hour >= 6:
                Label(master=root, text="Good Morning Bosss", font=("Roboto", 20)).place(x=490, y=180)
            elif 17 > now.hour >= 12:
                Label(master=root, text="Good Afternoon Bosss", font=("Roboto", 20)).place(x=490, y=180)
            elif 22 > now.hour >= 17:
                Label(master=root, text="Good Evening Bosss", font=("Roboto", 20)).place(x=490, y=180)
            Label(master=root, text="Your assistant is on the way", font=("Roboto", 20)).place(x=490, y=230)
            try:
                time.sleep(3)
                obj = Assist()
                obj.mainloop()

            except Exception as e:
                Label(master=root, text="your assistant currently facing some problem", font=("Roboto", 20)).place(x=490, y=280)
                Label(master=root, text=f"{e}", font=("Roboto", 20)).place(x=490, y=330)
    CTkLabel(master=root,text="Enter password to confirm", font=("Roboto", 20)).place(x=50,y=120)
    p_ver = StringVar()
    CTkEntry(master=root, font=("Roboto", 20),textvariable=p_ver,width=300).place(x=50,y=150)
    Button(master=root,text="Confirm", font=("Roboto", 20),command=confirm,relief=GROOVE,activebackground="#daded3",width=24).place(x=60,y=250)
    Button(master=root,text="ForgotPassword", font=("Roboto", 20),relief=GROOVE, activebackground="#daded3",width=24).place(x=60,y=320)
    root.mainloop()
