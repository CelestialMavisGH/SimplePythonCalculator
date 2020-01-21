import tkinter as tk
import os
from tkinter import *

# Simply declaring the main window "root" and changing the title as well as the icon.

root = tk.Tk()
root.title("Simplified Calculator using Python/Tkinter")
root.iconbitmap('award.ico')

# This canvas provides some sort of colored background on top of the roof window, it's a simple addition for some asthetics,
# Although usually you'll use a frame with this to make it look better

canvas = Canvas(root, height=600, width=600, bg="#6441a5")
canvas.grid(row=0, column=0)

# This is the only textbox in this program and it's called "Entry" in Tkinter, it's used to display the math operations

screen = Entry(canvas, width=35, bd=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Declaring the scrollbar

sidepa = Scrollbar(canvas, orient=VERTICAL)

# These global variables are the ones that govern which of the math symbol buttons do and is used in later code down

global ad
global mul
global sub
global div
ad = "ad"
mul = "mul"
sub = "sub"
div = "div"

# This function just simple writes out whatever numbers you click on and it's the only function for the numbers!

def button_click(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))


#list of buttons for the numbers

button_1 = Button(canvas, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(canvas, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(canvas, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(canvas, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(canvas, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(canvas, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(canvas, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(canvas, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(canvas, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(canvas, text="0", padx=40, pady=20, command=lambda: button_click(0))


# This is what the History tab on the right is made out of, a label, a listbox and a scrollbar, there is more code for it in other functions

sidepa.grid(row=1, column=3)
history = Listbox(canvas, yscrollcommand = sidepa.set)
history.grid(row=1, column=3, rowspan=3)
his = Label(canvas, text="HISTORY")
his.grid(row=0, column=3)

def buttonAdd(sth):

    # This primarily just saves the value of the screen at the moment you clicked any of those "+,*,-,/"
    # essentially this means the first number entered which then gets deleted from the textbox and saved into memory

    firstNum = screen.get()
    global fnum
    # We are using the global stat as a way to set the method of Math in the program, a very simple method
    global stat
    stat = str(sth)
    # This print is just for debugging what's going on in the background
    print("DEBUG PRINT: Math Mode has been changed to: " + stat)
    fnum = int(firstNum)
    screen.delete(0, END)

# We are declaring all the Math type buttons below

button_add = Button(canvas, text="+", padx=39, pady=20, command=lambda: buttonAdd(ad))
button_muti = Button(canvas, text="*", padx=39, pady=20, command=lambda: buttonAdd(mul))
button_sub = Button(canvas, text="-", padx=39, pady=20, command=lambda: buttonAdd(sub))
button_div = Button(canvas, text="/", padx=39, pady=20, command=lambda: buttonAdd(div))

# Simple clear function

def buttonClear():
    screen.delete(0, END)

# This function determines what the mode of Math is and conducts the process based on that.

def buttonEqual():
    secondval = screen.get()
    global secNum
    secNum = int(secondval)
    screen.delete(0, END)
    global histor
    add = '+'
    multiply = '*'

    if stat == "ad":
      screen.insert(0, fnum + secNum)
      histor = fnum + secNum
      history.insert(END, histor)
    else:
        print("DEBUG PRINT: This isn't an Addition")

    if stat == "mul":
     screen.insert(0, fnum * secNum)
     histor = fnum * secNum
     history.insert(END, histor)
    else:
        print("DEBUG PRINT: This isn't a multiplication")

    if stat == "sub":
     screen.insert(0, fnum - secNum)
     histor = fnum - secNum
     history.insert(END, histor)
    else:
        print("DEBUG PRINT: This isn't a Subtraction")

    if stat == "div":
     screen.insert(0, fnum / secNum)
     histor = fnum / secNum
     history.insert(END, histor)
    else:
        print("DEBUG PRINT: This isn't a Division")


# Declaring the buttons for the equal sign and clear

button_equal = Button(canvas, text="=", padx=88, pady=20, command=buttonEqual)

button_clear = Button(canvas, text="Clear", padx=79, pady=20, command=buttonClear)


# Attachs all the buttons to the grid/root

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_muti.grid(row=6, column=1)
button_sub.grid(row=6, column=0)
button_div.grid(row=6, column=2)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)



#Main loop to run the window

root.mainloop()

exit = input("Press any key to quit the applications")