from tkinter import *
from time import strftime
from tkinter.ttk import *
root = Tk()
root.geometry("500x300")
root.minsize(1000,250)
root.maxsize(200,1000)
root.wm_iconbitmap("clock.ico")
root.title("GRD_CLOCK_🕖")
def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000,time)
label1 = Label(text="Welcome To GRD's Time⏳ Clock",font=("Rubik Vinyl",30)).pack()
label = Label(root,background="#e4ebdd",foreground="#0c0d1c",font=("Roboto Mono",100),relief=SUNKEN)
label.pack(anchor='center',padx=100,pady=50)
time()
root.mainloop()