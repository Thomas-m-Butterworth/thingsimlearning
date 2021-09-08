## FIND A VIDEO OF WILLIAM SHATNER COUNTING, CREATE A LIBRARY AND THE NUMBER INPUT CALLS THAT FILE.
## USE WINSOUND TO CALL THE SOUND, HAVE WILLY SHATZ READING THE SCREEN

## The ANSWER variable to be used in an f-string of william shatner counts, so it always calls
## the right file using the syntax. 

from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number= e.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_number)
    e.delete(0, END)

def button_subtract():
    first_number= e.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number= e.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number= e.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    global f_num
    global s_num
    s_num = int(second_number)
    e.delete(0, END)
    if math == "add":
        answer = f_num + s_num
        e.insert(0, answer)
    elif math == "multiply":
        answer = f_num * s_num
        e.insert(0, answer)
    elif math == "divide":
        answer = f_num / s_num
        answer = int(answer)    # Dividing always results in a float, stopping continuity. This will round up
        e.insert(0, answer)
    elif math == "subtract":
        answer = f_num - s_num
        e.insert(0, answer)
    f_num = 0
    s_num = 0
    

# Calc Buttons
## Tkinter doesn't allow functions to pass arguments in a button. Use **lambda** to solve this.
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

add = Button(root, text="+", padx=39, pady=20, command=button_add)
clear = Button(root, text="C", padx=79, pady=20, command = button_clear)
equals = Button(root, text="=", padx=91, pady=20, command=button_equal)

subtract = Button(root, text="-", padx=39, pady=20, command=button_subtract)
multiply = Button(root, text="*", padx=39, pady=20, command=button_multiply)
divide = Button(root, text="/", padx=39, pady=20, command=button_divide)

# Buttons on screen
button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)

button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)

button_0.grid(row=4, column=0)
clear.grid(row=4, column=1, columnspan=2)

add.grid(row=5, column=0)
equals.grid(row=5, column=1, columnspan=2)

subtract.grid(row=6, column=0)
multiply.grid(row=6, column=1)
divide.grid(row=6, column=2)


# Initialise
root.mainloop()