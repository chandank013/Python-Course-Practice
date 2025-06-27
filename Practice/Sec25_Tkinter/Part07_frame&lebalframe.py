#lec(346-347)

from tkinter import *
from tkinter.messagebox import *
from turtle import right

from click import command


# Using class(OOP's)
class MyTop(Toplevel):

    def childhandler(self):
        showinfo('My', 'Child window message')

    def __init__(self):
        Toplevel.__init__(self)
        for i in range(0,3):
            for j in range(0,3):
                bt1=Button(self,text=str(i+j),padx=15,command=self.childhandler).grid(row=i,column=j ,padx=5)



def myhandler():

    tp1 =MyTop()
    tp1.geometry("300x300")
    tp1.title('Child Window')

    tp1.mainloop()


    # # Using simple coding
    # def child_handler():
    #     showinfo('My', 'Child window message')

    # tp1=Toplevel(win)
    # tp1.title("Child Window")
    # tp1.geometry("300x300")

    # bt=Button(tp1,text='Button 1', command=child_handler)
    # bt.pack()
    # tp1.mainloop()



# Frame wedgit  (They are act as container becouse it hold other wedget)

win = Tk()
win.geometry("600x400")


# # Frame wedgit  (They are act as container becouse it hold other wedget)
# f1 = Frame(win, bg = "red", width=300)
# f1.pack(side=LEFT, fill=Y)

# f1 = Frame(win, bg = "green", width=300)
# f1.pack(side=RIGHT, fill=Y)



# # Lebal frame wedgit
# f3 = LabelFrame(win, text="Frame 1", bg = "red", width=300)
# f3.pack(side=LEFT, fill=Y)

# f4 = LabelFrame(win,text="Frame 2", bg = "green", width=300)
# f4.pack(side=RIGHT, fill=Y)

# b1 = Button(f3,text="Button 1")
# b2 = Button(f3,text="Button 2")
# b3 = Button(f3,text="Button 3")
# b4 = Button(f3,text="Button 4")

# b1.grid(row=0, column=0)
# b2.grid(row=0, column=1)
# b3.grid(row=1, column=0)
# b4.grid(row=1, column=1)


# b11 = Checkbutton(f4,text="Button 11")
# b12 = Checkbutton(f4,text="Button 12")
# b13 = Checkbutton(f4,text="Button 13")
# b14 = Checkbutton(f4,text="Button 14")

# b11.pack()
# b12.pack()
# b13.pack()
# b14.pack()



# Toplebal Wedget (used to create child window)

b21 = Button(win, text="Click Me!", command= myhandler)
b21.pack()


win.mainloop()

