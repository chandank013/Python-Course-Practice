from tkinter import *

from click import option





# Create the option menu 

def cahnge(e):
    lstvar = Variable(value=dict1[var1.get()])
    lst1.delete(0, END)
    lst1.config(listvariable=lstvar)


win = Tk()
win.geometry("300x200")
win.title("Option Menu")


dict1= {
    "Language": ["Python", "Java", "C++"],
    "Database": ["MySQL", "MongoDB", "PostgreSQL"],
    "Clouds": ["AWS", "Azure", "Google Cloud"]}

var1 = StringVar(value="Language")
opt1 = OptionMenu(win, var1, *dict1.keys(), command=cahnge)
opt1['fg'] = 'blue'
opt1.pack()


lstvar1 = Variable(value=dict1["Language"])
lst1 = Listbox(win, listvariable=lstvar1, height=5, selectmode=MULTIPLE)
lst1.pack()                     


win.mainloop()