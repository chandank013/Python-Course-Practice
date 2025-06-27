# Tkinter:(304-308)
# Discriptions:


# from tkinter import *
# win = Tk()    # This line creating a window




# win.title('My First Application')

# win.geometry('600x400-0+0')   # It define the size of window in left corner  (length x breadth + x-axis + y-axis)

# win.resizable(False,True)   # Through this we can resize the window according to own choice

# win.attributes('-alpha',0.9)   # alpha is used to opaqueness of window


# # win.geometry('600x400-100-100')   # Window will comw in right corner
# # win.geometry('600x400+100-100')   # Window will comw in right corner
# # win.geometry('600x400-100+100')   # Window will comw in right corner

# win.mainloop()

# # Short code of avobe
# from tkinter import *
# win = Tk()
# win.geometry('600x400-0+0')  
# win.resizable(False,True) 
# win.attributes('-alpha',0.9)
# win.mainloop()






# # Adding a Tkinter widgets to window based application:
# from tkinter import *
# win = Tk()
# win.geometry('600x400-0+0')  
# win.resizable(False,True) 
# win.attributes('-alpha',1)


# l =Label(win, text = 'Enter your name:')   # Used to add text and image
# l.pack()


# e = Entry(win)    # Adding taxBox
# e.pack()


# b = Button(win, text = 'Click Me')  # Add the button
# b.pack()


# t = Text(win, width= 30, height= 10)     # Allow to enter the multiple line called as (Text Area)
# t.pack()


# # c = Checkbutton(win, text = 'Yes')
# # c.pack()


# c1 = Radiobutton(win, text = 'Option 01', variable= 'v1', value=1)
# c1.pack()
# c2 = Radiobutton(win, text = 'Option 02', variable= 'v1', value=2)
# c2.pack()
# c3 = Radiobutton(win, text = 'Option 03', variable= 'v1', value=3)
# c3.pack()   # Whenrver we use radio button then we have to use multiple button to select any one of them.


# v = StringVar()  # It help in showing the selected thing from Option Menu
# o = OptionMenu(win,v, 'var', 'Python', 'Jawa', 'C++', 'Python', 'Jawascript')
# o.pack()


# s =Scale(win, from_= 0, to= 100)  # Add Scale to the window
# s.pack()



# win.mainloop()






# Widgets Option (Common Properties of Wedgets) Code to set options in wedgets:
from tkinter import *
win = Tk()
win.geometry('600x400-0+0')

# # (text) option is available for various Wedgets
# l = Label(win, text= 'Hello World')
# l.pack()
#                 #or
# l = Button(win, text= 'Hello World')
# l.pack()
#                 #or
# l = Checkbutton(win, text= 'Hello World')
# l.pack()
#                 #or
# l = Radiobutton(win, text= 'Hello World')
# l.pack()


# # (bg) Common option for various control
# c = Checkbutton(win, text= 'Hello World', bg='red')
# c.pack()
               

# c = Label(win, text= 'Hello World', bg='red', fg='white') ## fg is used to set the color of text, bg is used to set the color of background
# c.pack()
#                 #or
# # (fg) Also common for various control (Label, Button, Checkbutton, Radiobutton) in dictionary pattern

# f = Label(win)  
# f['text']= 'Hello World'
# f['bg']='Black'
# f['fg']= 'white'
# f.pack()


# (Font)  common for various control(Label, Button, Checkbutton, Radiobutton)
c =Checkbutton(win, text= 'Hello World!',  bg='black', fg= 'white', width=10, variable='var')  # width , height is not for some wedgets like Entry, Text, Button
c['bd'] = 3   # With the help of this we make border of wedgets 
c['height'] = 5  # Help in definng Dimention .It id not for Entry
c['anchor']= 'ne'   # It help in defining the location of the wedgets it is not for Entry
c['justify']= 'right'   # It help in defining the location of the wedgets it is not for Entry
c['relief']= 'flat'  # It help in defining the location of the wedgets it is not for Entry
c.pack(padx=100) # help in pushing left ,right of wedgets
c.pack(pady=100)  # help in pushing up, dowm of wedgets
c.config(font='Ariel, 10', height=100)  # It help in choosing the font of sentances(METHOD III  for Entrying wedgets)
c.pack()



win.mainloop()




