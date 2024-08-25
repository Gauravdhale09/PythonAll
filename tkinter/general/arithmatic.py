from tkinter import *


def add():
    try:
        equal = int(num1E.get()) + int(num2E.get())
        Label(root, text=equal, borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)
    except Exception as e:
        Label(root, text="Error", borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)


def sub():
    try:
        equal = int(num1E.get()) - int(num2E.get())
        Label(root, text=equal, borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)
    except Exception as e:
        Label(root, text="Error", borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)


def mul():
    try:
        equal = int(num1E.get()) * int(num2E.get())
        Label(root, text=equal, borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)
    except Exception as e:
        Label(root, text="Error", borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)


def div():
    try:
        equal = int(num1E.get()) / int(num2E.get())
        Label(root, text=equal, borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)
    except Exception as e:
        Label(root, text="Error", borderwidth=2, relief=SOLID, padx=15, pady=4, bg="Black", fg="White",
              font='Oswald').grid(row=5, column=5)


root = Tk()
root.title("Arithmatic Operation")
root.geometry("700x250")
root.configure(bg='#a9bfc9')
root.minsize(700, 250)
root.maxsize(700, 250)
# frame  = Frame(root,relief=SUNKEN,borderwidth=4,pady=40,padx=200,bg='#a9bfc9')
# frame.pack(anchor='nw',pady=20)
num1 = Label(root, text="Number1:", bg='#a9bfc9', font='Oswald')
num2 = Label(root, text="Number2:", bg='#a9bfc9', font='Oswald')
num1.grid(row=0, column=0)
num2.grid(row=2, column=0)
varnum1 = StringVar()
varnum2 = StringVar()
varnum3 = IntVar()
num1E = Entry(root, textvariable=varnum1, relief=SUNKEN, bg='#a9bfc9', font='Oswald')
num2E = Entry(root, textvariable=varnum2, relief=SUNKEN, bg='#a9bfc9', font='Oswald')

num1E.grid(row=0, column=1)
num2E.grid(row=2, column=1)
Button(text="Addition", command=add, font='Oswald', pady=2).grid()
Button(text="Subtraction", command=sub, font='Oswald', pady=2).grid()
Button(text="Multiplication", command=mul, font='Oswald', pady=2).grid()
Button(text="Division", command=div, font='Oswald', pady=2).grid()
root.mainloop()
