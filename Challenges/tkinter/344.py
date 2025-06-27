import csv
from email.mime import text
from tkinter import *
from turtle import back

from httpx import head
from numpy import var
from pyparsing import col
from scipy.__config__ import show




# CSV data
def show_data(e):
    i = headings.index(var1.get())
    col_data = [d[i] for d in data]
    lst1.delete(0, END)
    lst1['listvariable'] = Variable(value=col_data)

win = Tk()
win.geometry("285x200")
win.title("CSV Data")

file_csv = open("C:/Users/Arjun/09_Data Analytics/data/iris.csv", "r")
reader = csv.reader(file_csv)

headings = next(reader)
data = []
for row in reader:
    data.append(row)

var1 = StringVar(value=headings[0])
opt1 = OptionMenu(win,var1, *headings, command=show_data)
opt1.pack()

eids = [d[0] for d in data]

lstvar1 = Variable(value=eids)
lst1 = Listbox(win,bg="lightblue",listvariable=lstvar1, height=10, width=20)
lst1.pack()

win.mainloop()