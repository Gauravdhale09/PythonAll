from tkinter import *
from tkinter import ttk
from tkcalendar import *
class Tree(Tk):
    def __init__(self):
        super(Tree, self).__init__()
        self.geometry("700x700+0+0")

        def add():
            print("gender=", combobox.get())
            print("Name=", e1_var.get())
            print("Fathers name=", e2_var.get())
            print("Last name=", e3_var.get())
            print("Mothers name=", e4_var.get())
            print("D. O. B = ", combobox_date.get()+" "+combobox_month.get()+" "+combobox_year.get())
        def reset():
            combobox.set("custom")
            combobox_date.set(1)
            combobox_month.set("january")
            combobox_year.set(2001)
            e1_var.set("")
            e2_var.set("")
            e3_var.set("")
            e4_var.set("")
        Label(master=self, text="Gender", font=("roboto", 10)).place(x=20,y=20)
        Label(master=self, text="Name", font=("roboto", 10)).place(x=20,y=60)
        Label(master=self, text="Fatherame", font=("roboto", 10)).place(x=20,y=100)
        Label(master=self, text="Last Name", font=("roboto", 10)).place(x=20,y=140)
        Label(master=self, text="Mothers Name", font=("roboto", 10)).place(x=20,y=180)
        Label(master=self, text="Date Of Birth", font=("roboto", 10)).place(x=350,y=25)
        Label(master=self, text="Date", font=("roboto", 10)).place(x=270,y=60)
        Label(master=self, text="Month", font=("roboto", 10)).place(x=270,y=100)
        Label(master=self, text="Year", font=("roboto", 10)).place(x=270,y=140)
        combobox = ttk.Combobox(master=self, font=("roboto", 10), state="readonly")
        combobox['values'] = ("male", "female", "custom")
        combobox.set("custom")
        combobox.place(x=70, y=20)
        combobox_date = ttk.Combobox(master=self, font=("roboto", 10), state="readonly")
        value_date = []
        for i in range(1,32):
            value_date.append(i)
        combobox_date['values'] = tuple(value_date)
        combobox_date.set(1)
        combobox_date.place(x=350, y=60)
        combobox_month = ttk.Combobox(master=self, font=("roboto", 10), state="readonly")
        combobox_month['values'] = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
        combobox_month.set("january")
        combobox_month.place(x=350, y=100)
        combobox_year = ttk.Combobox(master=self, font=("roboto", 10), state="readonly")
        value_year = []
        for i in range(1995, 2025):
            value_year.append(i)
        combobox_year['values'] = tuple(value_year)
        combobox_year.set(2001)
        combobox_year.place(x=350, y=140)
        e1_var = StringVar()
        e2_var = StringVar()
        e3_var = StringVar()
        e4_var = StringVar()
        Entry(master=self, font=("roboto", 10), relief=SUNKEN, textvariable=e1_var).place(x=110, y=60)
        Entry(master=self, font=("roboto", 10), relief=SUNKEN, textvariable=e2_var).place(x=110, y=100)
        Entry(master=self, font=("roboto", 10), relief=SUNKEN, textvariable=e3_var).place(x=110, y=140)
        Entry(master=self, font=("roboto", 10), relief=SUNKEN, textvariable=e4_var).place(x=110, y=180)

        Button(master=self, text="ADD", font=("roboto", 10), relief=GROOVE, command=add).place(x=70, y=250)
        Button(master=self, text="Reset", font=("roboto", 10), relief=GROOVE, command=reset).place(x=150, y=250)

        #===================================
        #Tree
        frome = Frame(master=self, bd=4, relief=RIDGE)
        frome.place(x=20, y=300, width=650, height=300)
        scroll_x = Scrollbar(master=frome, orient=HORIZONTAL)
        scroll_y = Scrollbar(master=frome, orient=VERTICAL)

        table = ttk.Treeview(master=frome, columns=("fname", "lname", "faname", "moname", "gender", "age"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=table.xview)
        scroll_y.config(command=table.yview)
        table.heading("fname", text="First Name")
        table.heading("lname", text="Fathers Name")
        table.heading("faname", text="Last Name")
        table.heading("moname", text="Mothers Name")
        table.heading("gender", text="Gender")
        table.heading("age", text="Age")
        table['show'] = 'headings'
        table.column("fname", width=150)
        table.column("lname", width=150)
        table.column("gender", width=150)
        table.column("age", width=150)
        table.pack(fill=BOTH, expand=1)

if __name__ == '__main__':
    root = Tree()
    root.mainloop()
