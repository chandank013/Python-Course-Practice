from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk
from referencing import Anchor



def myhandler():
 
    pass



# Canvas wedgit  (used for drawing or container oa a panel)

win = Tk()
win.geometry("600x400")

can1 = Canvas(win, bg='yellow', width=600, height=400)
can1.pack()

can1.create_arc(100,100,200,200,fill='red',width=10,outline='black', start=90, extent=180)
can1.create_text(50,50, text = 'Hello World!', fill='blue')

img1 = ImageTk.PhotoImage(Image.open("C:/Users/Arjun/01_Udemy_Python/Udemy Python/Practice/Sec25_Tkinter/ghibli_pic.png"))
can1.create_image(10,10 , image=img1, anchor=NW)

btn1=Button(win, text='Click Me!')
can1.create_window(200,200, window=btn1)

win.mainloop()

 