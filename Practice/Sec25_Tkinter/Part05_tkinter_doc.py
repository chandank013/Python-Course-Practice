# Tkinter Widgets(317-324)


from calendar import c
from operator import length_hint
from tkinter import *
from tkinter import messagebox
from tkinter.font import *
from pyparsing import C


win = Tk()
win.title("Tkinter Widgets")
win.geometry("600x400")


# # Widget highlight
# b1 = Entry(win, highlightbackground="red", highlightthickness=10, highlightcolor="yellow")
# b1.pack()

# b2 = Checkbutton(win, text="Button-2", indicatoron=False)
# b2.pack()



# # Widget State
# b1 = Entry(win, state=DISABLED, disabledbackground= 'red', disabledforeground= 'yellow')  # Disabled mean you can't click the button
# b1.pack()

# b3 = Listbox (win, activestyle= UNDERLINE) # used for active style
# b3.insert(0, "Item-0")
# b3.insert(1, "Item-1")
# b3.insert(2, "Item-2")
# b3.insert(3, "Item-3")
# b3.pack()

# b2 = Checkbutton(win, text="Button-2")
# b2.pack()



# # # Widget Options

# # Widget Style & Relief
# b1 = Button(win, text="Button-1", bd='4', bg='#111111', fg='#555555', relief= RAISED, overrelief= GROOVE)  # S means south
# b1.pack()


# # Text / Item Selection
# e1 = Entry(win, selectbackground="red", selectforeground="yellow", selectborderwidth=10)  # Select background and foreground color
# e1.pack()

# lb1 = Listbox(win,  selectbackground="red", selectforeground="yellow", selectborderwidth=10, exportselection= False)  # SINGLE means you can select only one item at a time
# lb1.insert(0, "Item-0")
# lb1.insert(1, "Item-1")
# lb1.insert(2, "Item-2")
# lb1.insert(3, "Item-3")
# lb1.pack()

# lb2 = Listbox(win,  selectbackground="red", selectforeground="yellow", selectborderwidth=10, exportselection= False)  # SINGLE means you can select only one item at a time
# lb2.insert(0, "Item-0")
# lb2.insert(1, "Item-1")
# lb2.insert(2, "Item-2")
# lb2.insert(3, "Item-3")
# lb2.pack()


# # Text Insertion Cursor
# e1 = Text(win, insertbackground="red", insertwidth=10, insertborderwidth= 5, insertontime=1000, insertofftime=2000, cursor = 'boat')  # Insert background color and width
# e1.pack()


# # Text Widget
# l1 = Label(win, text="TextWidgetIsUsedForCheakingWrapLength", width=100, wraplength=100) # for wraplength
# l1.pack()

# e1 = Text(win, wrap=WORD, spacing3=100)  # WORD means wrap the text to the next line
# e1.pack()


# # Numeric Options
# var = IntVar(value=20)

# s1 = Scale(win, from_=0,variable=var, to=100, length=200, tickinterval=10, orient= HORIZONTAL)  # for horizontal scale
# s1.pack()


# s2 = Spinbox(win, from_=0, to=100, format= '%2.5f')  # for horizontal scale
# s2.pack()



sb1 = Scrollbar(win, orient= VERTICAL)  # for horizontal scale
t1 = Text(win)  # for horizontal scale

t1.config(yscrollcommand=sb1.set)  # for horizontal scale
sb1.config(command=t1.yview)  # for horizontal scale

sb1.pack(side= RIGHT, fill= Y)
t1.pack(side= LEFT, fill= Y)



# # Widget graphics
# l1 = Label(win,  bitmap= "hourglass")  # for bitmap
# l1.pack()

# img = PhotoImage(file= 'C:/Users/Arjun/01_Udemy_Python/Udemy Python/Concept/Section 25 Tkinter\ghibli_pic.png')  # for image
# l2 = Label(win, text= "Lebal-1", image=img ) # for wraplength
# l2.pack( ) # for anchor





win.mainloop()

