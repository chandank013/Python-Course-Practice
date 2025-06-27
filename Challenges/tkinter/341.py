from tkinter import *

from click import command
import random



# Shuffle list

def shuffle_list():
    random.shuffle(langs)
    lst1.delete(0, END)
    var1 = Variable(value=langs)
    lst1.config(listvariable=var1)

def my_handler(event):
    lbl1['text'] = lst1.get(lst1.curselection())


win = Tk()
win.geometry("600x400")
win.title("Select Item")
win.config(bg="lightblue")

langs = ["Python", "Java", "C++", "JavaScript", "Ruby", "PHP", "Swift", "Go", "Kotlin", "Rust"]

lbl1 = Label(win, text="Select Item", font=("Times new Roman", 20), bg="lightblue")
lbl1.pack()

var = Variable(value=langs)
lst1 = Listbox(win, listvariable=var, font=("Times new Roman", 10), width=20, height=10,  selectmode=SINGLE)
lst1.pack()
lst1.bind("<<ListboxSelect>>", my_handler)


# for i in lang:    # grid method
#     lst1.insert(END, i)
# lst1.grid()

# button for shuffle
btn1 = Button(win, text="Shuffle", font=("Times new Roman", 10), command= shuffle_list)
btn1.pack()


win.mainloop()