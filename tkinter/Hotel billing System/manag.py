from tkinter import *
from time import strftime
import datetime as dt
import tkinter.messagebox as msg
from PIL import ImageTk
import tkinter.font as f
import os
import webbrowser


def send():
    pass


def total():
    try:
        t1 = int(E1_varq.get()) * int(5)
        Label(frame1, text=f'{t1}₹', fg="blue", font=(
            'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=420, width=120)
        t2 = int(E2_varq.get()) * int(7)
        Label(frame1, text=f'{t2}₹', fg="blue", font=(
            'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=480, width=120)
        t3 = int(E3_varq.get()) * int(9)
        Label(frame1, text=f'{t3}₹', fg="blue", font=(
            'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=540, width=120)
        t4 = int(E4_varq.get()) * int(15)
        Label(frame1, text=f'{t4}₹', fg="blue", font=(
            'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=600, width=120)
        t5 = int(E5_varq.get()) * int(15)
        Label(frame1, text=f'{t5}₹', fg="blue", font=(
            'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=660, width=120)
        t = t1 + t2 + t3 + t4 + t5
        lab_to = Label(frame1, text=f'{t}Rs', fg="blue", font=(
            'roboto', 23, 'bold'), background="#F3E5AB")
        lab_to.place(x=1320, y=720, width=120)
    except Exception as e:
        Label(frame1, text="error", fg="blue", font=('roboto', 20, 'bold'),
              background="#F3E5AB").place(x=1320, y=720, width=120)
        msg.showwarning("ERROR", "Calculation Error")

    def save():
        if var_E.get() != '':
            if 10 <= len(var_p.get()) <= 13:
                if lab_to.cget("text") != '':
                    filepath = os.path.join('c:/E-bill', "Ebill.txt")
                    if not os.path.exists('c:/E-bill'):
                        os.makedirs('c:/E-bill')
                    with open(filepath, "a") as p:
                        p.write("\nConsumerName:" + f'{var_E.get()}' + "\tPhoneNo.:" + f'{var_p.get()}' + "\tDate:" +
                                f'{label_d.cget("text")}' + "\tTime:" + f'{label.cget("text")}' + "\tBoughtOfPrice:" + f'{lab_to.cget("text")}\n')
                    var_E.set('')
                    var_p.set('+91')
                    E1_varq.set(0)
                    E2_varq.set(0)
                    E3_varq.set(0)
                    E4_varq.set(0)
                    E5_varq.set(0)
            else:
                msg.showwarning("PH.NO2", "Invalid Phone number")
        else:
            msg.showerror("Name", "Consumer Name Not Found")
    Button(frame1, image=photo_t, relief=FLAT, bd=0, background="#F3E5AB", cursor="hand2",
           activebackground='#F3E5AB', command=save).place(x=720, y=720, width=110)


bill = Tk()
bill.geometry('1920x1080')
bill.state('zoomed')
bill.title("E-Bill")
bill.wm_iconbitmap('49616_bill_invoice_method_payment_sales_icon.ico')
f1 = f.Font(family="Dancing Script", size=18)
photo_b = PhotoImage(file='mae-mu-AX_VWc7ORwY-unsplash.png')
la_back = Label(bill, image=photo_b).place(x=0, y=0)
frame1 = Frame(bill, background='#F3E5AB', highlightbackground='#7B3F00',
               highlightthickness=20).place(x=650, y=50, height=740, width=870)
name = Label(bill, text="Consumer Name", font=f1,
             background="#F3E5AB").place(y=120, x=900)
var_E = StringVar()
name_E = Entry(bill, font=18, relief=SOLID,
               textvariable=var_E).place(x=1100, y=120)
name1 = Label(bill, text="Phone-Number", font=f1,
              background="#F3E5AB").place(x=900, y=180)
var_p = StringVar()
name_p = Entry(bill, font=18, relief=SOLID,
               textvariable=var_p).place(x=1100, y=180)
var_p.set("+91")
photo_k = PhotoImage(file='bill.png')
la_f = Label(frame1, image=photo_k, relief=SUNKEN, bd=0).place(x=674, y=130)


def time():
    string = strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000, time)


label = Label(bill, foreground="black", background="#F3E5AB", font=f1)
label.place(x=1050, y=300)
time()
date = dt.datetime.now()
label_d = Label(bill, text=f'{date:%A %b %d %Y}',
                foreground="black", background="#F3E5AB", font=f1)
label_d.place(x=980, y=240)
list_co = ["Item", "Price", "Quantity", "Total"]
co_x = [720, 920, 1120, 1320]
for (i, j) in zip(list_co, co_x):
    Label(frame1, text=i, font=f1, background="#F3E5AB").place(
        x=j, y=360, width=120)
Label(frame1, text="---------------------------------------------------------------------------------------------------------------------",
      font=20, background="#F3E5AB").place(x=670, y=390)
Label(frame1, text="---------------------------------------------------------------------------------------------------------------------",
      font=20, background="#F3E5AB").place(x=670, y=700)
photo_se = PhotoImage(file='send.png')
b2 = Button(frame1, image=photo_se, relief=FLAT, background="#F3E5AB",
            bd=0, cursor="hand2", activebackground='#F3E5AB', command=send)
b2.place(x=920, y=720, width=110)
photo_t = PhotoImage(file='save.png')
b2 = Button(frame1, image=photo_t, relief=FLAT, bd=0,
            background="#F3E5AB", cursor="hand2", activebackground='#F3E5AB')
b2.place(x=720, y=720, width=110)
photo_sa = PhotoImage(file='Untitled.png')
b2 = Button(frame1, image=photo_sa, relief=FLAT, bd=0, background="#F3E5AB",
            cursor="hand2", activebackground='#F3E5AB', command=total)
b2.place(x=1120, y=720, width=110)
item_list = ["Tea", "Milk", "Coffee", "Samosa", "Kachori"]
iem_y = [420, 480, 540, 600, 660]
for i, j in zip(item_list, iem_y):
    Label(frame1, text=i, font=f1, background="#F3E5AB").place(
        x=720, y=j, width=120)
price_list = [5, 7, 9, 15, 15]
for i, j in zip(price_list, iem_y):
    Label(frame1, text=f'{i}₹', font=f1, background="#F3E5AB").place(
        x=920, y=j, width=120)
photo_set = PhotoImage(file='t.png')
photo_d = PhotoImage(file='database.png')
photo_p = PhotoImage(file='pro.png')


def set():
    def total():
        try:
            t1 = int(E1_varp.get()) * int(E1_varq.get())
            Label(frame1, text=f'{t1}₹', fg="blue", font=(
                'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=420, width=120)
            t2 = int(E2_varp.get()) * int(E2_varq.get())
            Label(frame1, text=f'{t2}₹', fg="blue", font=(
                'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=480, width=120)
            t3 = int(E3_varp.get()) * int(E3_varq.get())
            Label(frame1, text=f'{t3}₹', fg="blue", font=(
                'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=540, width=120)
            t4 = int(E4_varp.get()) * int(E4_varq.get())
            Label(frame1, text=f'{t4}₹', fg="blue", font=(
                'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=600, width=120)
            t5 = int(E5_varp.get()) * int(E5_varq.get())
            Label(frame1, text=f'{t5}₹', fg="blue", font=(
                'roboto', 20, 'bold'), background="#F3E5AB").place(x=1320, y=660, width=120)
            t = t1 + t2 + t3 + t4 + t5
            lab_to = Label(frame1, text=f'{t}Rs', fg="blue", font=(
                'roboto', 20, 'bold'), background="#F3E5AB")
            lab_to.place(x=1320, y=720, width=120)
        except Exception as e:
            Label(frame1, text="error", fg="blue", font=('roboto', 20, 'bold'),
                  background="#F3E5AB").place(x=1320, y=720, width=120)
            msg.showwarning("ERROR", "Calculation Error")

        def save():
            if var_E.get() != '':
                if 10 <= len(var_p.get()) <= 13:
                    if lab_to.cget("text") != '':
                        filepath = os.path.join('c:/E-bill', "Ebill.txt")
                        if not os.path.exists('c:/E-bill'):
                            os.makedirs('c:/E-bill')
                        with open(filepath, "a") as p:
                            p.write("\nConsumerName:" + f'{var_E.get()}' + "\tPhoneNo.:" + f'{var_p.get()}' + "\tDate:" +
                                    f'{label_d.cget("text")}' + "\tTime:" + f'{label.cget("text")}' + "\tBoughtOfPrice:" + f'{lab_to.cget("text")}\n')
                        var_E.set('')
                        var_p.set('+91')
                        E1_varq.set(0)
                        E2_varq.set(0)
                        E3_varq.set(0)
                        E4_varq.set(0)
                        E5_varq.set(0)
                else:
                    msg.showwarning("PH.NO2", "Invalid Phone number")
            else:
                msg.showerror("Name", "Consumer Name Not Found")
        Button(frame1, image=photo_t, relief=FLAT, bd=0, background="#F3E5AB", cursor="hand2",
               activebackground='#F3E5AB', command=save).place(x=720, y=720, width=110)

    def set1():
        # label_item
        list2 = [420, 480, 540, 600, 660]
        list3 = [E1_var, E2_var, E3_var, E4_var, E5_var]
        for (i, j) in zip(list3, list2):
            Label(frame1, textvariable=i, font=f1,
                  background="#F3E5AB").place(x=720, y=j, width=120)
        # label_price
        list1 = [E1_varp.get(), E2_varp.get(), E3_varp.get(),
                 E4_varp.get(), E5_varp.get()]
        for (i, j) in zip(list1, list2):
            Label(frame1, text=f'{i}₹', font=f1, background="#F3E5AB").place(
                x=920, y=j, width=120)
    Button(frame1, image=photo_sa, relief=FLAT, bd=0, background="#F3E5AB", command=total,
           cursor="hand2", activebackground='#F3E5AB').place(x=1120, y=720, width=110)
    Button(frame1, image=photo_t, relief=FLAT, bd=0, background="#F3E5AB",
           cursor="hand2", activebackground='#F3E5AB').place(x=720, y=720, width=110)
    E5_var = StringVar()
    E1_var = StringVar()
    E2_var = StringVar()
    E3_var = StringVar()
    E4_var = StringVar()
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E1_var).place(x=720, y=420, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E2_var).place(x=720, y=480, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E3_var).place(x=720, y=540, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E4_var).place(x=720, y=600, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E5_var).place(x=720, y=660, width=120)
    E5_varp = StringVar()
    E1_varp = StringVar()
    E2_varp = StringVar()
    E3_varp = StringVar()
    E4_varp = StringVar()
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E1_varp).place(x=920, y=420, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E2_varp).place(x=920, y=480, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E3_varp).place(x=920, y=540, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E4_varp).place(x=920, y=600, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E5_varp).place(x=920, y=660, width=120)
    E5_varq = IntVar()
    E1_varq = IntVar()
    E2_varq = IntVar()
    E3_varq = IntVar()
    E4_varq = IntVar()
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E1_varq).place(x=1120, y=420, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E2_varq).place(x=1120, y=480, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E3_varq).place(x=1120, y=540, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E4_varq).place(x=1120, y=600, width=120)
    Entry(frame1, font=f1, background="#F3E5AB",
          textvariable=E5_varq).place(x=1120, y=660, width=120)
    Button(frame1, image=photo_t, relief=FLAT, bd=0, background="#F3E5AB",
           activebackground='#F3E5AB', cursor="hand2", command=set1).place(x=720, y=720, width=110)


Button(frame1, image=photo_set, relief=FLAT, bd=0, background='#F3E5AB', activebackground='#F3E5AB',
       cursor='hand2', command=set).place(x=1400, y=270, width=100, height=100)


def data():
    path = 'file:///C:/E-bill/Ebill.txt'
    if not os.path.exists('c:/E-bill/Ebill.txt'):
        msg.showerror("NotFound", "Sorry your Database Not Found")
    else:
        webbrowser.open_new(path)


Button(frame1, image=photo_d, relief=FLAT, bd=0, background='#F3E5AB', activebackground='#F3E5AB',
       cursor='hand2', command=data).place(x=1400, y=170, width=100, height=100)
Label(frame1, image=photo_p, relief=FLAT, bd=0, background='#F3E5AB',
      activebackground='#F3E5AB', cursor='hand2').place(x=1400, y=70, width=100, height=100)
Label(bill, text="user", foreground="black",
      background="#F3E5AB", font=10).place(x=1425, y=156)
photo_s1 = PhotoImage(file='set1.png')
E5_varq = IntVar()
E1_varq = IntVar()
E2_varq = IntVar()
E3_varq = IntVar()
E4_varq = IntVar()
Entry(frame1, font=f1, background="#F3E5AB",
      textvariable=E1_varq).place(x=1120, y=420, width=120)
Entry(frame1, font=f1, background="#F3E5AB",
      textvariable=E2_varq).place(x=1120, y=480, width=120)
Entry(frame1, font=f1, background="#F3E5AB",
      textvariable=E3_varq).place(x=1120, y=540, width=120)
Entry(frame1, font=f1, background="#F3E5AB",
      textvariable=E4_varq).place(x=1120, y=600, width=120)
Entry(frame1, font=f1, background="#F3E5AB",
      textvariable=E5_varq).place(x=1120, y=660, width=120)
bill.mainloop()
