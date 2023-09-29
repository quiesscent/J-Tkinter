from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Drop Down")
def show():
    Label(root, text=clicked.get()).pack()
clicked = StringVar()
clicked.set("Monday")
drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday","Thursday", "Friday")
drop.pack()

Button(root, text="show selection", command=show).pack()
root.mainloop()