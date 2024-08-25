from tkinter import *
from ATM_p2 import *
def Mar():
    M=Tk()
    M.geometry("1000x600")
    M.configure(bg='#0c97e8')
    M.mainloop()
root=Tk()
root.geometry("1000x600")
root.configure(bg='#0c97e8')
l1 = Label(text="\nWelcome To G_R_D ATM--------G_R_D बँक मध्ये आपले स्वागत आहे",font=('Unbounded',20),bg='#0c97e8').pack()
l2 = Label(text="Insert Your Card first!-------प्रथम तुमचे ATM कार्ड टाका",font=('Unbounded',20),bg='#0c97e8').pack()
l3 = Label(text="Select language for further procedure-------पुढील प्रक्रियेसाठी भाषा निवडा",font=('Unbounded',20),bg='#0c97e8').pack()
B1 = Button(root,text="English",width=30,font=('bold',30),relief=SOLID,bg='gray',command=Eng)
B1.pack(pady=30)
B2 = Button(root,text='मराठी',width=30,font=('bold',30),relief=SOLID,bg='gray',command=Mar)
B2.pack(pady=30)


root.mainloop()