from tkinter import *




# Create the ColorSelection on the basis of RGB

def Change_color(e):
    r = red_var.get()
    g = green_var.get()
    b = blue_var.get()
    color_lbl1['bg']=f'#{r:02x}{g:02x}{b:02x}'

win = Tk()
win.geometry("285x200")
win.title("Color Selection")

# Create the color label showing the combined color
color_lbl1 = Label(win ,width=40,height=2, bg ='black')
color_lbl1.grid(row=0, column=0, columnspan=4, pady=10)


# Create the color label
lbl2 = Label(win ,text="Red", width=10,fg='red')
lbl2.grid(row=1, column=0,  pady=10)

lbl3 = Label(win ,text="Green", width=10,fg='green')
lbl3.grid(row=2, column=0, pady=10 )

lbl4 = Label(win ,text="Blue", width=10,fg='blue')
lbl4.grid(row=3, column=0, pady=10)


# scales for RGB values
red_var = IntVar(value=0)
scl1 = Scale(win, from_=0, to=255, orient=HORIZONTAL,variable=red_var, length=200,bg="red",fg='white', command=Change_color)
scl1.grid(row=1, column=1, columnspan=3)

green_var = IntVar(value=0)
scl2 = Scale(win, from_=0, to=255, orient=HORIZONTAL,variable=green_var, length=200,bg="green",fg='white', command=Change_color)
scl2.grid(row=2, column=1, columnspan=3)

blue_var = IntVar(value=0)
scl3 = Scale(win, from_=0, to=255, orient=HORIZONTAL,variable=blue_var, length=200,bg="blue",fg='white', command=Change_color)
scl3.grid(row=3, column=1, columnspan=3)



win.mainloop()