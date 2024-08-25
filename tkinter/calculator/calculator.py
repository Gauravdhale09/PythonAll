from tkinter import *
def cal(event):
    global scrvar
    text = event.widget.cget("text")
    if(text=="="):

        if(scrvar.get().isdigit()):
            value=int(scrvar.get())
        else:
            try:
                value=eval(scrvar.get())
            except Exception as e:
                value = 'Error'

        scrvar.set(value)
        Screen.update()
    elif(text=="AC"):
        scrvar.set("")
        Screen.update()
    else:
        scrvar.set(scrvar.get()+text)
        Screen.update()
def eql():
    global scrvar
    eval(scrvar.get())
    Screen.update()
root = Tk()
root.geometry("500x580")
root.maxsize(520,580)
root.minsize(520,580)
root.configure(bg="#a9bfc9")
root.title("GRD_Calculator")
root.wm_iconbitmap("Calculator_30001.ico")
f_main = Frame(root,bg='#505b5e',borderwidth=2,width=500,relief=SUNKEN)
scrvar = StringVar()
scrvar.set("")
Screen = Entry(f_main,textvariable=scrvar,font=('Chivo Mono',35),relief=SUNKEN,bg='#a4dbb3',borderwidth=8,width=18)
Screen.insert(0,"0")
Screen.pack(pady=20,padx=10)
#frame 1
f1=Frame(f_main,height=80,width=4000,bg='#424a32')
for i in range(7,10):
    b1 = Button(f1, text=f'{i}', height=2, width=4, font=('Unbounded', 20, 'bold'), bg='cyan', cursor="tcross")
    b1.bind('<Button-1>', cal)
    b1.pack(side=LEFT, padx=10, pady=10)
b1 = Button(f1,text='+',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='AC',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
f1.pack(pady=2)
#fram 2
f1=Frame(f_main,height=80,width=4000,bg='#424a32')
for i in range(4,7):
    b1 = Button(f1, text=f'{i}', height=2, width=4, font=('Unbounded', 20, 'bold'), bg='cyan', cursor="tcross")
    b1.bind('<Button-1>', cal)
    b1.pack(side=LEFT, padx=10, pady=10)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='-',height=2,width=4,font=('Unbounded',20),bg='cyan',cursor="tcross",highlightbackground='#424a32')
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='00',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
f1.pack(pady=2)
# fram3
f1=Frame(f_main,height=80,width=4000,bg='#424a32')
for i in range(1,4):
    b1 = Button(f1, text=f'{i}', height=2, width=4, font=('Unbounded', 20, 'bold'), bg='cyan', cursor="tcross")
    b1.bind('<Button-1>', cal)
    b1.pack(side=LEFT, padx=10, pady=10)
b1 = Button(f1,text='*',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='=',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross" ,command=eql)
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
f1.pack(pady=2)
#frame4
f1=Frame(f_main,height=80,width=4000,bg='#424a32')
b1 = Button(f1,text='%',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='0',height=2,width=4,font=('Rubik Vinyl',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='.',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Button(f1,text='/',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="tcross")
b1.bind('<Button-1>',cal)
b1.pack(side=LEFT,padx=10, pady=10)
b1 = Label(f1,text='GRD',height=2,width=4,font=('Unbounded',20,'bold'),bg='cyan',cursor="arrow",fg='white')
b1.bind()
b1.pack(side=LEFT,padx=10, pady=10)
f1.pack(pady=2)
f_main.pack(padx=8,pady=4)
root.mainloop()