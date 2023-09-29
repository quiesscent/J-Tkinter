from tkinter import *

root = Tk()
root.title("J Calculator")

e = Entry(root, width= 35, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def button(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def clear():
    e.delete(0, END)

def add():
    first = e.get()
    global first_num
    global math
    math = "addition"
    first_num = int(first)
    e.delete(0, END)

def divide():
    first = e.get()
    global first_num
    global math
    math = "division"
    first_num = int(first)
    e.delete(0, END)

def multiply():
    first = e.get()
    global first_num
    global math
    math = "multiplication"
    first_num = int(first)
    e.delete(0, END)

def subtract():
    first = e.get()
    global first_num
    global math
    math = "subtraction"
    first_num = int(first)
    e.delete(0, END)

def equal():
    second = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, first_num + int(second))
    if math == "subtraction":
        e.insert(0, first_num -  int(second))
    if math == "multiplication":
        e.insert(0, first_num * int(second))
    if math == "division":
        e.insert(0, first_num / int(second))


# Button definition

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: button(1))

button2 = Button(root, text="2", padx=40, pady=20, command=lambda: button(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: button(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: button(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: button(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: button(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: button(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: button(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: button(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: button(0))

add_button = Button(root, text="+", padx=40, pady=20, command=add).grid(row=5,column=0)
div_button = Button(root, text="/", padx=40, pady=20, command=divide).grid(row=5,column=1)
sub_button = Button(root, text="-", padx=40, pady=20, command=subtract).grid(row=4,column=1)
mul_button = Button(root, text="*", padx=40, pady=20, command=multiply).grid(row=4,column=2)
equal_button = Button(root, text="=", padx=40, pady=20, command=equal).grid(row=5,column=2)
clear_button = Button(root, text="clear", padx=80, pady=20, command=clear).grid(row=6,column=0, columnspan=2)
quit = Button(root, text="Exit", padx=40, pady=20,command=root.quit).grid(row=6, column=2)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)


button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)


button0.grid(row=4, column=0)
root.mainloop()
