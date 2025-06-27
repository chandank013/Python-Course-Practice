












from tkinter import *
from tkinter import font
from turtle import up

import comm
from numpy import var
from sklearn import base



# Base Conversion 

def update_label():
    if base_type.get()==1:
        lbl1['text'] = str(value)
    elif base_type.get()==2:
        lbl1['text'] = str(bin(value))
    elif base_type.get()==3:
        lbl1['text'] = str(oct(value))
    elif base_type.get()==4:
        lbl1['text'] = str(hex(value))
    


win = Tk()
win.geometry("450x100")
win.title("Font Options")

fnt = font.Font(size=15)

value = 35

lbl1 = Label(win, text=str(value), font=("Times new Roman", 45))
lbl1.grid(row=0, column=0, columnspan=4)

base_type = IntVar(value=0)

rdb1 = Radiobutton(win, text="Decimal", font=fnt, value=1, variable=base_type, command = update_label)
rdb1.grid(row=1, column=0)


rdb2 = Radiobutton(win, text="Binary", font=fnt, value=2, variable=base_type, command = update_label)
rdb2.grid(row=1, column=1)


rdb3 = Radiobutton(win, text="Octal", font=fnt, value=3, variable=base_type, command = update_label)
rdb3.grid(row=1, column=2)


rdb4 = Radiobutton(win, text="Hexadecimal", font=fnt, value=4, variable=base_type, command = update_label)
rdb4.grid(row=1, column=3)



win.mainloop()




