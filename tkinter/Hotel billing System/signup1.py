from tkinter import *
import tkinter.messagebox as msg

import tkinter as tk
from PIL import Image ,ImageTk
import string
import random
import tkinter.font as f
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017")
database = client['Signup']
coll = database['Addition']

def ok():
    if e1_var.get() != '':
        if e2_var.get() != '':
            if '@gmail.com' in e2_var.get():
                if 10 <= len(e3_var.get()) <= 13:
                    if len(e4_var.get()) == 6:
                        if e5_var.get() == e4_var.get():
                            z = coll.find_one({"E-mail id": e2_var.get()})
                            if z == None:
                                dict1 = {"Name": e1_var.get(), "E-mail id": e2_var.get(), "phone no.": e3_var.get(),
                                         "Password": e4_var.get()}
                                coll.insert_one(dict1)
                                root.destroy()
                         	import manag
                            else:
                                msg.showwarning(
                                    "Already Exists", "User of this Email already exists,go to login")
                        else:
                            msg.showwarning('warning', "Mismatch Passwords")
                    else:
                        msg.showinfo('note:', 'Password length must be 6')
                else:
                    msg.showwarning('Validity', 'Invalid phone number')
            else:
                msg.showwarning('Validity', 'Invalid Email')
        else:
            msg.showwarning('Empty', "Please Enter phone number!")
    else:
        msg.showwarning('Empty', "Please Enter your name!")


def gen():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = '@'
    all = lower+upper+num+symbol
    t = random.sample(all, 6)
    password = "".join(t)
    e4_var.set(password)


def sign():
    root.title('E-bill/Login')

    def log():
        if '@gmail.com' in e2_var.get() or e2_var.get() != '':
            if len(e4_var.get()) == 6:
                x = coll.find_one({"E-mail id": e2_var.get()})
                if x == None:
                    msg.showerror(
                        "Not found", "Email not found!,please register")
                else:
                    y = coll.find_one({"Password": e4_var.get()})
                    if y != None:
                        root.destroy()
                        import manag
                    else:
                        msg.showwarning(
                            'password', "Incorrect password,If you don't remember click on forgot password")
            else:
                msg.showinfo('note:', 'Password length must be 6')
        else:
            msg.showwarning('Validity', 'Invalid Email')
    frame1 = Frame(root, background='#c7d9d8').place(height=503, x=640, y=150, width=800)
    font = f.Font(family="Comic Sans MS", size=25, weight="bold")
    Label(frame1, text="LogIn", font=font,background='#c7d9d8').place(x=700, y=190)
    list1 = ["Email-Id", "Password"]
    row = [260, 330]
    for (i, j) in zip(list1, row):
        Label(frame1, text=i, font=('Roboto', 20, 'italic'),background='#c7d9d8').place(x=700, y=j)
    e2_var = StringVar()
    E2 = Entry(frame1, font=('Roboto', 15), width=30,
               textvariable=e2_var, relief=SOLID).place(x=950, y=260)
    e2_var.set('@gmail.com')
    e4_var = StringVar()
    E4 = Entry(frame1, font=('Roboto', 15), width=30,
               textvariable=e4_var, relief=SOLID).place(x=950, y=330)
    e5_var = StringVar()
    b1 = Button(frame1, image=photo_up, cursor='hand2',
                relief=FLAT, command=log, bd=0).place(x=700, y=450)
    b2 = Button(frame1, image=photo_re, bd=0, cursor='hand2',
                relief=FLAT, command=up).place(x=170, y=580, width=400)
    b3 = Button(frame1, text='Forgot Password?', fg='blue', relief=FLAT, background='#c7d9d8', cursor='hand2',
                bd=0, activeforeground='blue', activebackground='#c7d9d8', font=('Roboto', 17, 'bold')).place(x=850, y=400)


def up():
    root.title('E-bill/Register')

    def ok():
        if e1_var.get() != '':
            if e2_var.get() != '':
                if '@gmail.com' in e2_var.get():
                    if 10 <= len(e3_var.get()) <= 13:
                        if len(e4_var.get()) == 6:
                            if e5_var.get() == e4_var.get():
                                z = coll.find_one({"E-mail id": e2_var.get()})
                                if z == None:
                                    dict1 = {"Name": e1_var.get(), "E-mail id": e2_var.get(), "phone no.": e3_var.get(),
                                             "Password": e4_var.get()}
                                    coll.insert_one(dict1)
                                    root.destroy()
                                    import manag
                                else:
                                    msg.showwarning(
                                        "Already Exists", "User of this Email already exists,go to login")
                            else:
                                msg.showwarning(
                                    'warning', "Mismatch Passwords")
                        else:
                            msg.showinfo('note:', 'Password length must be 6')
                    else:
                        msg.showwarning('Validity', 'Invalid phone number')
                else:
                    msg.showwarning('Validity', 'Invalid Email')
            else:
                msg.showwarning('Empty', "Please Enter phone number!")
        else:
            msg.showwarning('Empty', "Please Enter your name!")
        print("Name:-" + e1_var.get() + "\tEmail-Id:" + e2_var.get() +
              "\tPhone-no.:" + e3_var.get() + "\tPassword:-" + e4_var.get())

    def gen():
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbol = '@'
        all = lower + upper + num + symbol
        t = random.sample(all, 6)
        password = "".join(t)
        e4_var.set(password)
    frame1 = Frame(root, background='#afd8db').place(
        height=503, x=640, y=150, width=800)
    Label(frame1, text="Register", font=font,
          background='#afd8db').place(x=700, y=190)
    list1 = ["Full-Name", "Email-id", "Phone no.",
             "Password", "Confirm-password"]
    row = [260, 330, 400, 470, 540]
    for (i, j) in zip(list1, row):
        Label(frame1, text=i, font=('Roboto', 20, 'italic'),
              background='#afd8db').place(x=700, y=j)
    e1_var = StringVar()
    E1 = Entry(frame1, font=('Roboto', 15, 'italic'), width=30,
               textvariable=e1_var, relief=SOLID).place(x=950, y=260)
    e2_var = StringVar()
    E2 = Entry(frame1, font=('Roboto', 15), width=30,
               textvariable=e2_var, relief=SOLID).place(x=950, y=330)
    e2_var.set('@gmail.com')
    e3_var = StringVar()
    E3 = Entry(frame1, font=('Roboto', 15), width=30,
               textvariable=e3_var, relief=SOLID).place(x=950, y=400)
    e3_var.set('+91')
    e4_var = StringVar()
    E4 = tk.Entry(frame1, font=('Roboto', 15), width=30,
                  textvariable=e4_var, relief=SOLID)
    E4.place(x=950, y=470)
    c1_var = IntVar(value=0)

    def show():
        E4.config(show="")

        def hide():
            E4.config(show="*")
            Button(frame1, image=photo_s, command=show,
                   bd=0, relief=SUNKEN).place(x=1200, y=471)

        Button(frame1, image=photo_h, command=hide,
               bd=0, relief=SUNKEN).place(x=1200, y=471)

    def hide():
        E4.config(show="*")

        def show():
            E4.config(show="")
            Button(frame1, image=photo_h, command=hide,
                   bd=0, relief=SUNKEN).place(x=1200, y=471)
    Button(frame1, image=photo_s, command=show,
           bd=0, relief=SUNKEN).place(x=1200, y=471)
    e5_var = StringVar()
    E5 = Entry(frame1, font=('Roboto', 15), width=30,
               textvariable=e5_var, relief=SOLID).place(x=950, y=540)

    def info():
        info = Tk()
        info.geometry('500x100')
        info.wm_iconbitmap('49616_bill_invoice_method_payment_sales_icon.ico')
        info.config(background='yellow')
        info.title('E-bill/help')
        info.maxsize(500, 100)
        info.minsize(500, 100)
        Label(info, text='Hello user, welcome to E-bill version 1.o\nIf you already have an account click on LogIn',
              background='yellow', font=20).pack()

        def close():
            info.destroy()
        Button(info, text="Ok", background='lightblue', activebackground='lightblue',
               font=20, relief=SOLID, command=close).pack(pady=10)
    bu_in = Button(frame1, image=photo_in, relief=FLAT, bd=0, background='#afd8db',
                   activebackground='#afd8db', command=info).place(x=1380, y=160)
    b1 = Button(frame1, image=photo_si, cursor='hand2', relief=FLAT,
                bd=0, command=ok).place(x=700, y=590, width=200, height=50)
    l2 = Button(frame1, text="*Generate password", font=('Roboto', 22, 'italic'), bd=0, background='#afd8db', fg='blue',
                activebackground='#afd8db', activeforeground='blue', cursor='hand2', width=30, relief=FLAT, command=gen).place(y=580, x=900)
    b2 = Button(frame1, image=photo_log, bd=0, cursor='hand2', width=30,
                relief=FLAT, command=sign).place(x=170, y=580, width=400)


root = Tk()
root.state('zoomed')
root.geometry('2000x2000')
root.wm_iconbitmap('49616_bill_invoice_method_payment_sales_icon.ico')
root.title('E-bill/Register')
font = f.Font(family="Comic Sans MS", size=25, weight="bold")
photo = Image.open('door.png')
p = photo.resize((1500, 996))
photo_r = ImageTk.PhotoImage(p)
Label(root, image=photo_r).place(x=0, y=0, relheight=1, relwidth=1)
img = Image.open('signup.png')
img_r = img.resize((500, 500))
img_n = ImageTk.PhotoImage(img_r)
Le_f = Label(root, image=img_n).place(y=150, x=140)
frame1 = Frame(root, background='#afd8db').place(
    height=503, x=640, y=150, width=800)
Label(frame1, text="Register", font=font,
      background='#afd8db').place(x=700, y=190)
Label3 = Label(root, text="@GRD-python🐍Dev.", font=("Unbounded",
               11), background="white").place(x=140, y=150)
list1 = ["Full-Name", "Email-id", "Phone no.", "Password", "Confirm-password"]
row = [260, 330, 400, 470, 540]
for (i, j) in zip(list1, row):
    Label(frame1, text=i, font=('Roboto', 20, 'italic'),
          background='#afd8db').place(x=700, y=j)
e1_var = StringVar()
E1 = Entry(frame1, font=('Roboto', 15, 'italic'), width=30,
           textvariable=e1_var, relief=SOLID).place(x=950, y=260)
e2_var = StringVar()
E2 = Entry(frame1, font=('Roboto', 15), width=30,
           textvariable=e2_var, relief=SOLID).place(x=950, y=330)
e2_var.set('@gmail.com')
e3_var = StringVar()
E3 = Entry(frame1, font=('Roboto', 15), width=30,
           textvariable=e3_var, relief=SOLID).place(x=950, y=400)
e3_var.set('+91')
e4_var = StringVar()
E4 = tk.Entry(frame1, font=('Roboto', 15), width=30,
              show='*', textvariable=e4_var, relief=SOLID)
E4.place(x=950, y=470)
c1_var = IntVar(value=0)


def show():
    E4.config(show="")

    def hide():
        E4.config(show="*")
        Button(frame1, image=photo_s, command=show,
               bd=0, relief=SUNKEN).place(x=1200, y=471)
    Button(frame1, image=photo_h, command=hide,
           bd=0, relief=SUNKEN).place(x=1200, y=471)


def hide():
    E4.config(show="*")

    def show():
        E4.config(show="")
        Button(frame1, image=photo_h, command=hide,
               bd=0, relief=SUNKEN).place(x=1200, y=471)
    Button(frame1, image=photo_s, command=show,
           bd=0, relief=SUNKEN).place(x=1200, y=471)


photo_h = PhotoImage(file='hide.png')
photo_s = PhotoImage(file='show.png')
c1 = Button(frame1, image=photo_s, command=show,
            bd=0, relief=SUNKEN).place(x=1200, y=471)
e5_var = StringVar()
E5 = Entry(frame1, font=('Roboto', 15), width=30,
           textvariable=e5_var, relief=SOLID).place(x=950, y=540)
photo_si = PhotoImage(file='signup1.png')
b1 = Button(frame1, image=photo_si, cursor='hand2', relief=FLAT,
            bd=0, command=ok).place(x=700, y=590, width=200, height=50)
l2 = Button(frame1, text="*Generate password", fg='blue', font=('Roboto', 22, 'italic'), bd=0, background='#afd8db',
            activebackground='#afd8db', activeforeground='blue', cursor='hand2', width=30, relief=FLAT, command=gen).place(y=580, x=900)
photo_log = PhotoImage(file='log.png')
photo_re = PhotoImage(file='register.png')
photo_up = PhotoImage(file='login1.png')
photo_in = PhotoImage(file='info.png')


def info():
    info = Tk()
    info.geometry('500x100')
    info.wm_iconbitmap('49616_bill_invoice_method_payment_sales_icon.ico')
    info.config(background='yellow')
    info.title('E-bill/help')
    info.maxsize(500, 100)
    info.minsize(500, 100)
    Label(info, text='Hello user, welcome to E-bill version 1.o\nIf you already have an account click on LogIn',
          background='yellow', font=20).pack()

    def close():
        info.destroy()
    Button(info, text="Ok", background='lightblue', activebackground='lightblue',
           font=20, relief=SOLID, command=close).pack(pady=10)


bu_in = Button(frame1, image=photo_in, relief=FLAT, bd=0, background='#afd8db',
               activebackground='#afd8db', command=info).place(x=1380, y=160)
b2 = Button(frame1, image=photo_log, cursor='hand2', bd=0, width=30,
            relief=FLAT, command=sign).place(x=170, y=580, width=400)
root.mainloop()
