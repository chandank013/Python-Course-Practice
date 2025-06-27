# Tkinter: (312-314)
# # Event Handling

# from tkinter import *
# def on_click():  # Define the event handler function
#     print("Button is clicked!")

# win = Tk()
# win.title("Event Handling")

# win.geometry("600x400")

# b1 = Checkbutton(win, text="My Button", bg="red", fg="yellow", command=on_click) 
# b1.pack()

# b1 = Checkbutton(win, text="My Button", bg="red", fg="yellow", command=lambda: on_click('Cheak button is clicked!'))
# b1.pack()

# win.mainloop()



# # Event binding on instance of a widget
# from tkinter import *
# from tkinter.messagebox import *

# # Event binding on instance of a widget

# def fun(e):  # Define the event handler function
#     showinfo("My Box", "Event is triggered!")  # Show a message box

# win = Tk()
# win.title("Event Binding")
# win.geometry("600x400")

# e = Entry(win, bg="lightblue", fg="blue")
# e.place(x=100, y=100, width=200, height=50)

# e.bind('<KeyPress>', fun)  # Bind the event to the widget instance


# win.mainloop()



# # Event binding on instance of a widget using shift key

# from tkinter import *
# from tkinter.messagebox import *

# # Event binding on instance of a widget

# def fun(e):  # Define the event handler function
#     showinfo("My Box", "Event is triggered!")  # Show a message box

# win = Tk()
# win.title("Event Modifier")
# win.geometry("600x400")

# e = Entry(win, bg="lightblue", fg="blue")
# e.place(x=100, y=100, width=200, height=50)

# e1 = Entry(win, bg="lightblue", fg="blue")
# e1.place(x=100, y=160, width=200, height=50)

# e.bind('<Button-1>', fun)  # Bind the event to the widget instance
# e1.bind('<Button-1>', fun)  # Bind the event to the widget instance

# win.mainloop()



# Event binding using class (for every widget handler to work upon the same class)
# from tkinter import *
# from tkinter.messagebox import *

# def fun(e):  # Define the event handler function
#     showinfo("My Box", "Event is triggered!")  # Show a message box

# win = Tk()
# win.title("Event Modifier")
# win.geometry("600x400")

# e = Entry(win, bg="red", fg="yellow")
# e.place(x=100, y=100, width=200, height=50)

# e1 = Entry(win, bg="lightblue", fg="blue")
# e1.place(x=100, y=160, width=200, height=50)

# e2 = Entry(win, bg="green", fg="blue")
# e2.place(x=100, y=220, width=200, height=50)

# # win.bind_class('Entry','<Button-1>', fun)  # Bind the event to the widget instance


# # Application level event binding mean to bind the event to the whole application
# win.bind_all('<Button-1>', fun)  # Bind the event to the widget instance

# win.mainloop()



# # Event binding using class (for every widget handler to work upon the same class)

# from tkinter import *
# from tkinter.messagebox import *

# def fun(e):  # Define the event handler function
#     showinfo("My Box", "Event is triggered!")  # Show a message box

# def fun1(e):  # Define the event handler function
#     showinfo("My Box", e.char)  # Show a message box

# win = Tk()
# win.title("Event Modifier")
# win.geometry("600x400")

# e = Entry(win, bg="red", fg="yellow")
# e.place(x=100, y=100, width=200, height=50)

# e.bind('<Button-1>', fun) 
# e.bind('<KeyPress>', fun1, add='+')  # Bind the event to the widget instance

# win.mainloop()