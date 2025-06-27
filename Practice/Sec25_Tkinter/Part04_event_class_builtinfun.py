# Event Class and Built-in Functions
# Tkinter:(115,116)

# from tkinter import *
# from tkinter import messagebox

# def my_handler(e):
#     # print(e)

#     # # KeyPress event
#     print(e.char)
#     print(e.keysym_num)
#     print(e.keysym)
#     print(e.type)

#     # # Button event
#     # print(e.state)
#     # print(e.x_root, e.y_root)

# win = Tk()
# win.title("Event Class and Built-in Functions")
# win.geometry("600x400")

# ent = Entry(win)
# ent.pack()

# # ent.bind("<Button-1>", my_handler)
# ent.bind("<KeyPress>", my_handler)

# win.mainloop()




# Event handler function: the function which responds to the event
# cget: get the value of a widget option(available in all the widget)

from tkinter import *
from tkinter.messagebox import *


def my_handler(e):
    # print(lbl.cget("text")) # get the value of text option

    if e.type == "7": # left mouse button click event
    # using dictory method(for Enter)
        lbl["bg"] = "blue" # change the value of bg option
        lbl["text"] = "blue color" # change the value of text option
    elif e.type == "8": # left mouse button click event
        lbl["bg"] = "red" # change the value of bg option
        lbl["text"] = "red color" # change the value of text option

    print(e.type) # print the type of event
    print(type(e.type)) # print the type of event


    # using cget method(for button)
    # showinfo("My Info", lbl.cget("bg")) # get the value of text option
    # lbl.config(bg="white") # change the value of bg 
    

    # # using dictory method(for button)
    # showinfo("My Info", lbl["bg"]) # get the value of text option
    # lbl["bg"] = "white" # change the value of bg option

   


win = Tk()
win.title("Event Class and Built-in Functions")
win.geometry("600x400")

lbl = Label(win, text="red color", bg="red", width=20, height=2)
lbl.pack()
lbl.bind("<Enter>", my_handler) # left mouse button click event
lbl.bind("<Leave>", my_handler,add='+') # left mouse button click event



win.mainloop()



# conclusion:
#  also i have handle the multiple event by defining two handler function also combining the two event in one function
# use of e.type to identify the event type
# use of cget method to get the value of widget option