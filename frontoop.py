from tkinter import *
from backoop import database

database=database("books.db")
class Window():
    def __init__(self, window):
        self.window=window
        self.window.wm_title("Bookstore")
        l1=Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2=Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3=Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4=Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        self.input1=StringVar()
        self.e1=Entry(window, textvariable=self.input1)
        self.e1.grid(row=0, column=1)

        self.input2=StringVar()
        self.e2=Entry(window, textvariable=self.input2)
        self.e2.grid(row=0, column=3)

        self.input3=StringVar()
        self.e3=Entry(window, textvariable=self.input3)
        self.e3.grid(row=1, column=1)

        self.input4=StringVar()
        self.e4=Entry(window, textvariable=self.input4)
        self.e4.grid(row=1, column=3)

        self.list1=Listbox(window, height=6, width=35)
        self.list1.grid(row=2,column=0, rowspan=6, columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.getrows)

        b1=Button(window, text="view all", width=12, command=self.view_command)
        b1.grid(row=2,column=3)

        b2=Button(window, text="search entry", width=12, command=self.search_command)
        b2.grid(row=3,column=3)

        b3=Button(window, text="add entry", width=12, command=self.add_command)
        b3.grid(row=4,column=3)

        b4=Button(window, text="update", width=12, command=self.update_command)
        b4.grid(row=5,column=3)

        b5=Button(window, text="delete", width=12, command=self.delete_command)
        b5.grid(row=6,column=3)

        b6=Button(window, text="close", width=12, command=self.window.destroy)
        b6.grid(row=7,column=3)

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.input1.get(),self.input2.get(),self.input3.get(),self.input4.get()):
            self.list1.insert(END,row)
    def add_command(self):
        self.list1.delete(0,END)
        database.insert(self.input1.get(),self.input2.get(),self.input3.get(),self.input4.get())
        self.list1.insert(END,(self.input1.get(),self.input2.get(),self.input3.get(),self.input4.get()))

    def getrows(self,event):

        try:
            index=self.list1.curselection()[0]
            self.selectedrow=self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,self.selectedrow[1])
            self.e2.delete(0,END)
            self.e2.insert(END,self.selectedrow[2])
            self.e3.delete(0,END)
            self.e3.insert(END,self.selectedrow[3])
            self.e4.delete(0,END)
            self.e4.insert(END,self.selectedrow[4])
        except IndexError:
            pass
    def delete_command(self):
        database.delete(self.selectedrow[0])

    def update_command():
        database.update(self.selectedrow[0], self.input1.get(), self.input2.get(), self.input3.get(), self.input4.get())




window=Tk()
Window(window)
window.mainloop()
