
from tkinter import *
from time import strftime



# Project (337)-Digital-Clock

def myclock():
    time = strftime('%H:%M:%S %p') # 24-hour format with AM/PM
    lbl1.config(text=time)
    lbl1.after(100, myclock)  # Update the clock every second

win = Tk()
win.title("Digital Clock")
win.geometry("400x200")

lbl1 = Label(win, font=("calibri", 40, "bold"), background="red")
lbl1.pack(fill=BOTH, expand=1)  # Fill the label to the window and expand it


myclock()  # Call the function to start the clock
win.mainloop() # Start the main loop of the window

