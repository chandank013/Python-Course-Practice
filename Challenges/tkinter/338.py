from tkinter import *
from time import strftime



# Project (338)-Stopwatch

elepse_time = 0  # Variable to store elapsed time
flag = True  # Flag to control the stopwatch

def start():  # Function to start the stopwatch
    global flag, elepse_time
    flag = True  # Set the flag to True to indicate the stopwatch is running
    update_time()  # Call the update function to start the stopwatch

def update_time():  # Function to update the time on the label
    global elepse_time, flag
    if flag == True:
        elepse_time += 1
        milli = elepse_time % 1000
        sec= (elepse_time // 1000) % 60
        minute = (elepse_time // 60000) % 60
        sec = sec % 60

        lbl1['text'] = f"{minute:02d}:{sec:02d}:{milli:03d}"  # Update the label with the formatted time
        lbl1.after(1, update_time)  # Call the update function again after 1 millisecond

def stop():  # Function to stop the stopwatch
    global flag
    flag = False  # Set the flag to False to indicate the stopwatch is stopped
 
def reset():  # Function to reset the stopwatch
    global elepse_time, flag
    flag = False  # Set the flag to False to indicate the stopwatch is stopped
    elepse_time = 0  # Reset the elapsed time to 0
    lbl1['text'] = "00:00:000"  # Update the label to show the reset time



win = Tk()
win.title("Stopwatch")  
win.geometry("250x120")

lbl1 = Label(win,text="00:00:000",font=("calibri", 45, "bold"))
lbl1.grid(row=0, column=0, columnspan=3)  # Position the label in the grid

btn1 = Button(win, text="Start", command=start)  # Start button
btn1.grid(row=1, column=0)  # Position the button in the grid

btn2 = Button(win, text="Stop", command=stop)  # Stop button
btn2.grid(row=1, column=1)  # Position the button in the grid

btn3 = Button(win, text="Reset", command=reset)  # Reset button
btn3.grid(row=1, column=2)  # Position the button in the grid



win.mainloop() # Start the main loop of the window
