from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("400x400")
root.minsize(400, 400)

f1 = Frame(root, bg="Blue", borderwidth=6, relief=SUNKEN, pady=100)
f1.pack(side=RIGHT, fill=Y, pady=42, padx=41)
GRD = Label(f1, text="Hii GAURAV How are you?", padx=22, pady=56)
GRD.pack()
# image = Image.open("GRD.jpg")
# photo  =ImageTk.PhotoImage(image)
#
# Lebel = Label(image=photo)
# Lebel.pack()

GRD.pack()
root.mainloop()
