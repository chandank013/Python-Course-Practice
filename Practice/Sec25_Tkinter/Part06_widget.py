from email.policy import default
from logging.handlers import MemoryHandler
from multiprocessing import parent_process
from pydoc import text
import re
from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
from turtle import back
from xml.sax import handler
import tkinter.messagebox as msg
import tkinter as tk
import comm
from matplotlib.pylab import pareto
from numpy import var
from tkinter.filedialog import *


# # Practice 01 (Check Button Widget)
# def myhandler():  
#     lbl['text'] = cb1['text'] if var1.get() == 1 else " "
#     lbl['text'] += cb2['text'] if var2.get() == 1 else " "
#     lbl['text'] += cb3['text'] if var3.get() == 1 else " "

# def buthandler():
#     cb1.invoke() 


# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# # Radio Button Widget and Check Button Widget are used for selecting one option from multiple options

# lbl = Label(win, text=" ")
# lbl.pack()

# var1 = IntVar()
# cb1 = Checkbutton(win, text="Java", variable=var1, command= myhandler)
# cb1.pack()

# var2 = IntVar()
# cb2 = Checkbutton(win, text="Python", variable=var2, command= myhandler)
# cb2.pack()

# var3 = IntVar()
# cb3 = Checkbutton(win, text="C++", variable=var3, command= myhandler)
# cb3.pack()


# win.mainloop()




# # Practice 02 (Radio Button Widget)
# def myhandler():  
#     lbl['text'] = var.get()
#     if var.get() == "Java":
#         messagebox.showinfo("Info", "You selected Java")
#     elif var.get() == "Python":
#         messagebox.showinfo("Info", "You selected Python")
#     elif var.get() == "C++":
#         messagebox.showinfo("Info", "You selected C++")


# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# # Radio Button Widget and Check Button Widget are used for selecting one option from multiple options

# lbl = Label(win, text=" ")
# lbl.pack()

# var = StringVar()
# cb1 = Radiobutton(win, text="Java", variable=var,value='Java', command= myhandler)
# cb1.pack()

# cb2 = Radiobutton(win, text="Python", variable=var,value='Python', command= myhandler)
# cb2.pack()

# cb3 = Radiobutton(win, text="C++", variable=var,value='C++', command= myhandler)
# cb3.pack()


# win.mainloop()






# # Practice 03 (Lebal and Button widget)
# def myhandler():  
#     var.set(var.get() + 1)


# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# # Radio Button Widget and Check Button Widget are used for selecting one option from multiple options

# fnt = Font(family="Courier", size=30)

# var = IntVar(value=0)
# lbl = Label(win, text="0",textvariable=var, font=fnt, fg="blue", bg="yellow")
# lbl.pack()

# but1 = Button(win, text="Click to Count",font = fnt, fg="yellow", bg="blue", command=myhandler)
# but1.pack()

# win.mainloop()



# # Practice 04 (Listbox and Button widget)
# def myhandler(e):  
#     var.set(lst1.curselection())


# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# var = StringVar()
# ent1 = Entry(win,textvariable=var, width=15, font=("Arial", 12))
# ent1.pack()


# lst1 = Listbox(win, selectmode=EXTENDED, width=20, height=10)
# lst1.insert(1, "Java")
# lst1.insert(2, "Python")
# lst1.insert(3, "C++")
# lst1.insert(4, "C#")
# lst1.insert(5, "JavaScript")
# lst1.insert(6, "PHP")
# lst1.insert(7, "Ruby")
# lst1.insert(8, "Swift")
# lst1.insert(9, "Go")
# lst1.insert(10, "Kotlin")
# lst1.insert(11, "Rust")
# lst1.insert(12, "Dart")
# lst1.insert(13, "Scala")
# lst1.insert(14, "Perl")
# lst1.insert(15, "Lua")
# lst1.insert(16, "Haskell")
# lst1.insert(17, "Elixir")
# lst1.insert(18, "Clojure")
# lst1.insert(19, "F#")
# lst1.insert(20, "Objective-C")
# lst1.insert(21, "Visual Basic")
# lst1.insert(22, "Assembly")
# lst1.insert(23, "COBOL")
# lst1.insert(24, "Fortran")
# lst1.insert(25, "Ada")
# lst1.insert(26, "R")
# lst1.insert(27, "MATLAB")
# lst1.insert(28, "Julia")
# lst1.insert(29, "Scheme")
# lst1.insert(30, "Prolog")
# lst1.insert(31, "Smalltalk")
# lst1.insert(32, "Scratch")
# lst1.insert(33, "Logo")
# lst1.insert(34, "ActionScript")
# lst1.insert(35, "VBScript")
# lst1.pack()

# sb1 = Scrollbar(win, orient= VERTICAL)  # for horizontal scale


# lst1.config(yscrollcommand=sb1.set)  # for horizontal scale
# sb1.config(command=lst1.yview)  # for horizontal scale

# sb1.pack(side= RIGHT, fill= Y)

# btn1 = Button(win, text="Click Me", )
# btn1.pack()

# lst1.bind("<<ListboxSelect>>", myhandler) # Bind the selection event to the variable

# # lst1.itemconfig(1, background="red", foreground="white") # Change the color of the first item
# # lst1.select_set(3, 5) # Select items 3 to 5
# # lst1.see(15) # Scroll to the 15th item
# win.mainloop()





# # Practice 05 (Spinbox widget)

# def myhandler():
#     spb1.selection_get('range',0,3)

# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# lst1 = ['Amazon', 'Myntra', 'Flipkart', 'Snapdeal', 'eBay', 'Alibaba', 'Walmart', 'Best Buy', 'Target', 'Costco']

# var1 = StringVar()
# ent1 = Entry(win, textvariable=var1, width=15, font=("Arial", 12))
# ent1.pack()


# spb1 = Spinbox(win, from_=0.0, to=100.0,increment=0.01, width=10, font=("Arial", 12), fg="blue", bg="yellow", values=lst1)
# spb1.pack()

# btn1 = Button(win, text="Click Me", font=("Arial", 12), fg="yellow", bg="blue", command=myhandler)
# btn1.pack()


# win.mainloop()




# # Practice 06 (Scale widget)

# # def myhandler():

# def myhandler(e):
#     f = Font(size=str(scl1.get()))
#     ent1['font'] = f

# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# var1 = StringVar(value='Hello World')
# ent1 = Entry(win, textvariable=var1)
# ent1.pack()

# scl1 = Scale(win, from_=10, to=50, orient=VERTICAL, fg="white", bg="black",resolution=5, tickinterval=10, showvalue=0, command=myhandler)
# scl1.pack()


# win.mainloop()






# # Practice 07 (Entry widget) used for password and username

# def myhandler(txt):
#     if txt.isdigit():
#         return False
#     else:
#         return True
    
# win = Tk()
# win.title("My Window")
# win.geometry("600x400")

# hand1 = (win.register(myhandler), '%S') # %S is the string that is being inserted into the entry widget

# var1 = StringVar(value='Hello World')
# ent1 = Entry(win, textvariable=var1,validate="key", validatecommand=hand1 )
# ent1.pack()


# # # methods of Entry widget
# # ent1.insert(0, "AAAA") # Insert text at the beginning
# # ent1.delete(0, 2) # Delete text from the beginning to the 2nd character


# win.mainloop()





# # Practice 08 (Text widget) 

# def myhandler():
#     print(txt1.get(1.0, 2.4)) # Get the text from the text widget

# def myhandler1():
#     txt1.edit_redo() # Undo the last action
    
# win = Tk()
# win.title("My Window")
# win.geometry("600x400")


# sc1 = Scrollbar(win, orient=VERTICAL)  # for horizontal scale
# sc1.pack(side=RIGHT, fill=Y)

# txt1 = Text(win, undo=True, wrap=WORD, yscrollcommand=sc1.set) # wrap=WORD is used to wrap the text at word boundaries
# txt1.pack(side=LEFT)

# sc1['command'] = txt1.yview # for horizontal scale

# bt1 = Button(win, text="Undo", command=myhandler)
# bt1.pack()

# bt2 = Button(win, text="Redo", command=myhandler1)
# bt2.pack()

# win.mainloop()






# # Practice 09 (Creating Menu bar) 


# def myhandler():
#     txt1.insert(1.0, "Hello World") # Insert text at the beginning

# def pophandler(e):
#     file.tk_popup(e.x_root, e.y_root, 0) # Show the popup menu at the mouse position

# win = Tk()
# win.geometry("600x400")

# txt1 = Text(win) 
# txt1.pack(fill=BOTH)

# menubar = Menu(win)
# win['menu'] = menubar

# file = Menu(menubar, tearoff=0) # tearoff=0 is used to remove the line that separates the menu from the window
# menubar.add_cascade(label="File", menu=file) # Add the file menu to the menubar

# file.add_command(label="New") # Add a new command to the file menu
# file.add_command(label="Open", command=myhandler) # Add an open command to the file menu
# file.add(itemType= 'command',label="Save") # Add a save command to the file menu
# file.add_separator() # Add a separator line to the file menu
# file.add_checkbutton(label="Save As", onvalue=1,offvalue=0) # Add a checkbutton to the file menu


# rad1 = Menu(file) # Create a submenu for the file menu
# rad1.add_radiobutton(label='Option 1') # Add a radiobutton to the submenu
# rad1.add_radiobutton(label='Option 2') # Add a radiobutton to the submenu
# rad1.add_radiobutton(label='Option 3') # Add a radiobutton to the submenu
# file.add_cascade(label="Options", menu=rad1) # Add the submenu to the file menu


# txt1.bind("<Button-2>", pophandler)


# win.mainloop()




# # Practice 10 (Message Box) 
# def myhandler():
#     ans = msg.askquestion("My", "Do you want to Continue?" , default='no', parent = win) # Show an info message box
#     print(ans) # Print the answer to the console


# win = Tk()
# win.geometry("600x400")

# btn1 = tk.Button(win, text="Click Me", command=myhandler)
# btn1.pack()

# win.mainloop()





# Practice 11 (File Dialog Widget) 

def openhandler():
    fname = askopenfile()
    txt = fname.read()
    text1.insert(1.0, txt) # Insert text at the beginning

def savehandler():
    fname = asksaveasfile()
    fname.write(text1.get(1.0, 'end-1c')) # Write text to the file
    fname.close()

def clearhandler():
    text1.delete(1.0, 'end-1c') # Delete all text from the text widget

win = Tk()
win.geometry("600x400")

text1 = Text(win)
text1.pack()

btn1 = Button(win, text="Open", command=openhandler)
btn1.pack()
btn2 = Button(win, text="Save", command=savehandler)
btn2.pack()
btn3 = Button(win, text="Clear", command=clearhandler)
btn3.pack()



win.mainloop()