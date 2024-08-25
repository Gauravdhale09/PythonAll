from customtkinter import *
from tkinter import *
import tkinter.messagebox as msg
import random
from PIL import Image,ImageTk
from playsound import playsound

def ok():
    if E1_var.get() != "":
        CTkLabel(master=root, text=f"{E1_var.get()} Vs Computer",width=300, text_color="white", font=("roboto", 25)).place(x=150,
                                                                                                                 y=130)
        CTkLabel(master=root, text=f"{E1_var.get()}",width=100, text_color="white", font=("roboto", 25)).place(x=80,
                                                                                                                 y=200)

    else:
        CTkLabel(master=root, text=f"Player Vs Computer",width=300, text_color="white", font=("roboto", 25)).place(x=150,y=130)
        CTkLabel(master=root, text=f"Player", width=100, text_color="white", font=("roboto", 25)).place(x=80,y=200)
def play(x):
    win = Toplevel()
    win.geometry('500x200+460+300')
    win.title("Result")
    win.wm_iconbitmap('icon.ico')

    def close():
        win.destroy()

    CTkButton(master=win, text="OK", command=close).place(x=350, y=150)
    win.config(bg="black")
    CTkLabel(master=win, text="Computer", text_color="white", font=("roboto", 15)).place(x=340, y=5)
    if E1_var.get() != "":
        CTkLabel(master=win, text=f"{E1_var.get()}", text_color="white", font=("roboto", 15)).place(x=100, y=5)
    else:
        CTkLabel(master=win, text="Player", text_color="white", font=("roboto", 15)).place(x=100, y=5)
    generate = random.randint(0, 2)

    if x == 1:
        Label(win, image=img1).place(x=50, y=30)
        if generate == 0:
            Label(win, image=img1).place(x=300, y=30)
            CTkLabel(master=win, text="Match Draw 👊", text_color="white", font=('roboto', 20)).place(x=130, y=130)
            try:
                playsound('lose.mp3')
            except:
                playsound('lose.mp3')
        elif generate == 1:
            Label(win, image=img2).place(x=300, y=30)
            CTkLabel(master=win, text="You won 👍", text_color="white", font=('roboto', 20)).place(x=130, y=130)
            try:
                playsound('winner.mp3')
            except:
                playsound('winner.mp3')

        else:
            Label(win, image=img3).place(x=300, y=30)
            CTkLabel(master=win, text="You lose 👎", text_color="white", font=('roboto', 20)).place(x=130, y=130)
            try:
                playsound('lose.mp3')
            except:
                playsound('lose.mp3')
    elif x==2:
        Label(win, image=img2).place(x=50, y=30)
        if generate == 0:
            Label(win, image=img1).place(x=300, y=30)
            CTkLabel(master=win, text="You lose 👎", text_color="white", font=('roboto', 20)).place(x=130, y=150)
            try:
                playsound('lose.mp3')
            except:
                playsound('lose.mp3')
        elif generate == 1:
            Label(win, image=img2).place(x=300, y=30)
            CTkLabel(master=win, text="Match Draw 👊", text_color="white", font=('roboto', 20)).place(x=130, y=150)
            try:
                playsound('lose.mp3')
            except:
                playsound('lose.mp3')
        else:
            Label(win, image=img3).place(x=300, y=30)
            CTkLabel(master=win, text="You won 👍", text_color="white", font=('roboto', 20)).place(x=130, y=150)
            try:
                playsound('winner.mp3')
            except:
                playsound('winner.mp3')
    else:
        Label(win, image=img3).place(x=50, y=30)
        if generate == 0:
            Label(win, image=img1).place(x=300, y=30)
            CTkLabel(master=win, text="You won 👍", text_color="white", font=('roboto', 20)).place(x=130, y=150)
            try:
                playsound('winner.mp3')
            except:
                playsound('winner.mp3')
        elif generate == 1:
            Label(win, image=img2).place(x=300, y=30)
            CTkLabel(master=win, text="You lose 👎", text_color="white", font=('roboto', 20)).place(x=130, y=150)

            try:
                playsound('lose.mp3')
            except:
                playsound('lose.mp3')
        else:
            Label(win, image=img3).place(x=300, y=30)
            CTkLabel(master=win, text="Match Draw 👊", text_color="white", font=('roboto', 20)).place(x=130, y=150)
            try:
                playsound('lose.mp3')
            except:
                playsound('lose.mp3')
    win.mainloop()
root = Tk()
root.geometry('600x700+420+50')
root.title('Snake-Water-Gun')
root.wm_iconbitmap('icon.ico')
root.config(bg="black")
CTkLabel(master=root,text="Welcome to Snake-Water-Gun game",text_color="white",font=("roboto", 20)).place(x=130,y=20)
CTkLabel(master=root,text="Enter your name",text_color="white",font=("roboto", 15)).place(x=130,y=80)
E1_var = StringVar()
CTkEntry(master=root,textvariable=E1_var, font=("roboto", 15, "bold")).place(x=250, y=80)
CTkButton(master=root,text="Play", width=50, corner_radius=20, command=ok).place(x=400,y=80)
CTkLabel(master=root, text=f"Computer", width=100, text_color="white", font=("roboto", 25)).place(x=420, y=200)
img1 = PhotoImage(file='snake.png')
img2 = PhotoImage(file="water.png")
img3 = PhotoImage(file="gun.png")
b1_var = IntVar()
b1=Button(root,image=img1, command=lambda x=1 :play(x), cursor='hand2').place(x=50, y=250)
b2=Button(root,image=img2, command=lambda x=2 :play(x), cursor='hand2').place(x=50, y=350)
b3=Button(root,image=img3, command=lambda x=3 :play(x), cursor='hand2').place(x=50, y=470)
Label(root,image=img1).place(x=400, y=250)
Label(root,image=img2).place(x=400, y=350)
Label(root,image=img3).place(x=400, y=470)
CTkLabel(master=root, text="Note:just click on the image", text_color="white", font=("roboto", 15)).place(x=400,y=670)
CTkLabel(master=root, text="Vs", text_color="white", font=("roboto", 60)).place(x=265,y=360)
root.mainloop()