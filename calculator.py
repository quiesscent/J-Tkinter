from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("J Calculator")

e = Entry(root, width=35, borderwidth=4)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def info():
    messagebox.showinfo('Calculator App', '''This is a python tkinter simple
    calculator by Jussie on his Journey through codes''')


def button(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def clear():
    e.delete(0, END)


def add():
    first = e.get()
    global first_num
    first_num = int(first)
    e.delete(0, END)


def equal():
    second = e.get()
    e.delete(0, END)
    e.insert(0, first_num + int(second))


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

add_button = Button(root, text="+", padx=40, pady=20, command=add).grid(row=5, column=0)
equal_button = Button(root, text="=", padx=92, pady=20, command=equal).grid(row=4, column=1, columnspan=3)
clear_button = Button(root, text="clear", padx=80, pady=20, command=clear).grid(row=5, column=1)
info = Button(root, text='info', command=info).grid(row=5, column=3)

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
