# Tkinter: (309-311)

# Geometry Management: pack(), grid(), place()
# pack() - packs widgets in the order they are added to the parent widget
# grid() - arranges widgets in a grid (rows and columns)
# place() - places widgets at an absolute position (x, y) in the parent widget
# pack() is the most commonly used geometry manager in Tkinter.

from tkinter import *
from turtle import left

from cv2 import LINE_4

win = Tk()
win.title("Geometry Management")
win.geometry("600x400")

# Pack Geometry Manager

# if u want to set wedet along the boundry use side=TOP, LEFT, RIGHT, BOTTOM
# l1 = Label(win, text="Label 1", bg="red", fg="yellow")
# l1.pack(side=LEFT) 
# l2 = Label(win, text="Label 2", bg="red", fg="yellow")
# l2.pack(side=TOP) 
# l3 = Label(win, text="Label 3", bg="red", fg="yellow")
# l3.pack(side=RIGHT)
# l4 = Label(win, text="Label 4", bg="red", fg="yellow")
# l4.pack(side=BOTTOM)


# if u want to set wedet at different position use anchor=N, S, E, W, NE, NW, SE, SW, CENTER
# l1 = Label(win, text="Label 5", bg="red", fg="yellow")
# l1.pack(anchor=NW) # North West
# l2 = Label(win, text="Label 6", bg="red", fg="yellow")
# l2.pack(anchor=NE) # North East
# l3 = Label(win, text="Label 7", bg="red", fg="yellow")
# l3.pack(anchor=SW) # South West
# l4 = Label(win, text="Label 8", bg="red", fg="yellow")
# l4.pack(anchor=SE) # South East
# l5 = Label(win, text="Label 9", bg="red", fg="yellow")
# l5.pack(anchor=CENTER) # Center
# l6 = Label(win, text="Label 10", bg="red", fg="yellow")
# l6.pack(anchor=W) # West
# l7 = Label(win, text="Label 11", bg="red", fg="yellow")
# l7.pack(anchor=E) # East
# l8 = Label(win, text="Label 12", bg="red", fg="yellow")
# l8.pack(anchor=N) # North
# l9 = Label(win, text="Label 13", bg="red", fg="yellow")
# l9.pack(anchor=S) # South


# # use padding to set the space between the widget and the parent widget
# l1 = Label(win, text="Label 14", bg="red", fg="yellow")
# l1.pack(padx=2, pady=2, ipadx=5, ipady=5) # padx and pady are the space between the widget and the parent widget, ipadx and ipady are the space between the widget and the text inside the widget
# l2 = Label(win, text="Label 15", bg="red", fg="yellow")
# l2.pack(padx=2, pady=2, ipadx=5, ipady=5) 
# l3 = Label(win, text="Label 16", bg="red", fg="yellow")
# l3.pack(padx=2, pady=2, ipadx=5, ipady=5) 


# # use fill to set the space between the widget and the parent widgetwidget
# l1 = Label(win, text="Label 14", bg="red", fg="yellow")
# l1.pack(side=LEFT, padx=2,fill=Y, pady=2, ipadx=15, ipady=15) # padx and pady are the space between the widget and the parent widget, ipadx and ipady are the space between the widget and the text inside the widget
# l2 = Label(win, text="Label 15", bg="red", fg="yellow")
# l2.pack(side=TOP, padx=2, fill=X, pady=2, ipadx=5, ipady=5) 
# l3 = Label(win, text="Label 16", bg="red", fg="yellow")
# l3.pack(side=LEFT, padx=2, pady=2, ipadx=5, ipady=5) 
# l4 = Label(win, text="Label 17", bg="red", fg="yellow")
# l4.pack(side=LEFT, padx=2, pady=2, ipadx=5, ipady=5)


# # Grid Geometry Manager

# l1 = Label(win, text="Label 1", bg="lightblue", fg="blue")
# l2 = Label(win, text="Label 2", bg="lightblue", fg="blue")
# l3 = Label(win, text="Label 3", bg="lightblue", fg="blue")
# l4 = Label(win, text="Label 4", bg="lightblue", fg="blue")
# l5 = Label(win, text="Label 5", bg="lightblue", fg="blue")
# l6 = Label(win, text="Label 6", bg="lightblue", fg="blue")
# l7 = Label(win, text="Label 7", bg="lightblue", fg="blue")
# l8 = Label(win, text="Label 8", bg="lightblue", fg="blue")
# l9 = Label(win, text="Label 9", bg="lightblue", fg="blue")

# l1.grid(row=0, column=0,columnspan=2, padx=5, pady=5)
# #l2.grid(row=0, column=1, padx=5, pady=5)
# l3.grid(row=0, column=2, padx=5, pady=5)

# l4.grid(row=1, column=0,rowspan=2, padx=5, pady=5)
# l5.grid(row=1, column=1, padx=5, pady=5)
# l6.grid(row=1, column=2, padx=5, pady=5)

# #l7.grid(row=2, column=0, padx=5, pady=5)
# l8.grid(row=2, column=1, padx=5, pady=5)
# l9.grid(row=2, column=2, padx=5, pady=5)


# Place Geometry Manager

# b1 = Button(win, text="Button 1", bg="red", fg="yellow")
# b1.place(x=100, y=100, width=150, height=100) # x and y are the position of the widget in the parent widget, width and height are the size of the widget
# b2 = Button(win, text="Button 2", bg="red", fg="yellow")
# b2.place(x=250, y=200, width=150, height=100)
# b3 = Button(win, text="Button 3", bg="red", fg="yellow")
# b3.place(x=400, y=300, width=150, height=100) 


b4 = Button(win, text="Button 4", bg="red", fg="yellow")
b4.place(relx=0.5, rely=0.5, relwidth=0.20, relheight=0.10)

win.mainloop()