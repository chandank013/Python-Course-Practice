# from tkinter import *


# drawing = None

# def first_point(e):
#     global drawing
#     pressflag.set(True)
#     x1.set(e.x)
#     y1.set(e.y)
#     x2.set(e.x)
#     y2.set(e.y)
#     draw_shape()

# def dragging(e):
#     if pressflag.get()==True:
#         can1.coords(drawing,x1.get(),y1.get(),e.x,e.y)

# def second_point(e):
#     can1.coords(drawing,x1.get(),y1.get(),e.x,e.y)
#     pressflag.set(False)


# def draw_shape():
#     global drawing
#     funs=[can1.create_line,can1.create_rectangle,can1.create_oval]
#     if shape_var.get()==0:
#         drawing=funs[shape_var.get()](x1.get(),y1.get(),x2.get(),y2.get(), fill = color_var.get(), width=width_var.get())
#     else:
#         drawing = funs[shape_var.get()](x1.get(),y1.get(),x2.get(),y2.get(), outline=color_var.get(), width=width_var.get())




# win = Tk()
# win.geometry("600x400")
# win.title('MS PAINT')

# can1 = Canvas(win, bg='#ffffbb',width=600, height=400)
# can1.pack(fill=BOTH,expand=True)
# can1.bind('<ButtonPress>', first_point)
# can1.bind('<ButtonRelease>', second_point)
# can1.bind('<Motion>', dragging)


# shape_var= IntVar(value=0)
# color_var=StringVar(value='red')
# width_var= IntVar(value=0)

# x1 = IntVar(value=0)
# y1 = IntVar(value=0)
# x2 = IntVar(value=0)
# y2 = IntVar(value=0)
# pressflag = BooleanVar(value=False)

# menubar = Menu(win)


# shape_menu = Menu(menubar)
# shape_menu.add_radiobutton(label='Line', variable=shape_var, value=0)
# shape_menu.add_radiobutton(label='Rectangle', variable=shape_var, value=1)
# shape_menu.add_radiobutton(label='Oval', variable=shape_var, value=2)
# menubar.add_cascade(label='Shapes', menu = shape_menu)


# color_menu = Menu(menubar)
# color_menu.add_radiobutton(label='red', variable=color_var, value='red')
# color_menu.add_radiobutton(label='green', variable=color_var, value='green')
# color_menu.add_radiobutton(label='blue', variable=color_var, value='blue')
# menubar.add_cascade(label='Colors', menu = color_menu)


# width_menu = Menu(menubar)
# width_menu.add_radiobutton(label=1, variable=width_var, value=1)
# width_menu.add_radiobutton(label=3, variable=width_var, value=3)
# width_menu.add_radiobutton(label=5, variable=width_var, value=5)
# menubar.add_cascade(label='Thikness', menu = width_menu)




# win['menu'] = menubar

# win.mainloop()


from tkinter import *

drawing = None
undo_stack = []  # Stack to store actions for undo
redo_stack = []  # Stack to store actions for redo

def first_point(e):
    global drawing
    pressflag.set(True)
    x1.set(e.x)
    y1.set(e.y)
    x2.set(e.x)
    y2.set(e.y)
    if eraser_mode.get():  # If eraser mode is active, start erasing immediately
        drawing = can1.create_line(e.x, e.y, e.x, e.y, fill=can1['bg'], width=width_var.get())
    else:
        draw_shape()

def dragging(e):
    if pressflag.get():
        if eraser_mode.get():  # If eraser mode is active
            can1.create_line(x1.get(), y1.get(), e.x, e.y, fill=can1['bg'], width=width_var.get())
            x1.set(e.x)
            y1.set(e.y)
        else:
            can1.coords(drawing, x1.get(), y1.get(), e.x, e.y)

def second_point(e):
    global drawing
    if not eraser_mode.get():  # Only update the shape if not in eraser mode
        can1.coords(drawing, x1.get(), y1.get(), e.x, e.y)
        # Save the action details to the undo stack
        undo_stack.append({
            "type": shape_var.get(),
            "coords": (x1.get(), y1.get(), e.x, e.y),
            "color": color_var.get(),
            "width": width_var.get(),
            "id": drawing
        })
        redo_stack.clear()  # Clear the redo stack after a new action
    pressflag.set(False)

def draw_shape():
    global drawing
    funs = [can1.create_line, can1.create_rectangle, can1.create_oval]
    if shape_var.get() == 0:
        drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(), fill=color_var.get(), width=width_var.get())
    else:
        drawing = funs[shape_var.get()](x1.get(), y1.get(), x2.get(), y2.get(), outline=color_var.get(), width=width_var.get())

def toggle_eraser():
    if eraser_mode.get():
        can1.config(cursor="circle")  # Change cursor to a circle (eraser-like symbol)
    else:
        can1.config(cursor="arrow")  # Change cursor back to default arrow

def undo_action():
    if undo_stack:  # Check if there are actions to undo
        last_action = undo_stack.pop()  # Remove the last action from the undo stack
        can1.delete(last_action["id"])  # Delete the last action from the canvas
        redo_stack.append(last_action)  # Add the action to the redo stack

def redo_action():
    if redo_stack:  # Check if there are actions to redo
        last_action = redo_stack.pop()  # Remove the last action from the redo stack
        # Redraw the action on the canvas
        funs = [can1.create_line, can1.create_rectangle, can1.create_oval]
        if last_action["type"] == 0:
            new_id = funs[last_action["type"]](
                *last_action["coords"], fill=last_action["color"], width=last_action["width"]
            )
        else:
            new_id = funs[last_action["type"]](
                *last_action["coords"], outline=last_action["color"], width=last_action["width"]
            )
        last_action["id"] = new_id  # Update the ID of the recreated item
        undo_stack.append(last_action)  # Add the action back to the undo stack

win = Tk()
win.geometry("600x400")
win.title('MS PAINT')

can1 = Canvas(win, bg='#ffffbb', width=600, height=400)
can1.pack(fill=BOTH, expand=True)
can1.bind('<ButtonPress>', first_point)
can1.bind('<ButtonRelease>', second_point)
can1.bind('<Motion>', dragging)

shape_var = IntVar(value=0)
color_var = StringVar(value='red')
width_var = IntVar(value=1)  # Thickness variable
eraser_mode = BooleanVar(value=False)  # Variable to track eraser mode

x1 = IntVar(value=0)
y1 = IntVar(value=0)
x2 = IntVar(value=0)
y2 = IntVar(value=0)
pressflag = BooleanVar(value=False)

menubar = Menu(win)

# Shape menu
shape_menu = Menu(menubar)
shape_menu.add_radiobutton(label='Line', variable=shape_var, value=0)
shape_menu.add_radiobutton(label='Rectangle', variable=shape_var, value=1)
shape_menu.add_radiobutton(label='Oval', variable=shape_var, value=2)
menubar.add_cascade(label='Shapes', menu=shape_menu)

# Color menu
color_menu = Menu(menubar)
color_menu.add_radiobutton(label='red', variable=color_var, value='red')
color_menu.add_radiobutton(label='green', variable=color_var, value='green')
color_menu.add_radiobutton(label='blue', variable=color_var, value='blue')
menubar.add_cascade(label='Colors', menu=color_menu)

# Width menu
width_menu = Menu(menubar)
width_menu.add_radiobutton(label=1, variable=width_var, value=1)
width_menu.add_radiobutton(label=3, variable=width_var, value=3)
width_menu.add_radiobutton(label=5, variable=width_var, value=5)
menubar.add_cascade(label='Thickness', menu=width_menu)

# Eraser menu
eraser_menu = Menu(menubar)
eraser_menu.add_checkbutton(label='Eraser', variable=eraser_mode, command=toggle_eraser)
eraser_menu.add_separator()  # Add a separator
eraser_menu.add_radiobutton(label='1', variable=width_var, value=1)
eraser_menu.add_radiobutton(label='5', variable=width_var, value=5)
eraser_menu.add_radiobutton(label='10', variable=width_var, value=10)
menubar.add_cascade(label='Eraser', menu=eraser_menu)

# Undo/Redo menu
edit_menu = Menu(menubar)
edit_menu.add_command(label='Undo', command=undo_action)
edit_menu.add_command(label='Redo', command=redo_action)
menubar.add_cascade(label='Edit', menu=edit_menu)

win['menu'] = menubar

win.mainloop()
