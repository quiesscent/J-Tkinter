from tkinter import *
from PIL import ImageTk, Image

"""In this program we are going to create a check box"""
root = Tk()
root.title("Check Boxes")
root.geometry("400x400")


def show():
    Label(root, text=var.get()).pack()


# var = IntVar()
var = StringVar()
check = Checkbutton(root, text="Check me", variable=var, offvalue="Off", onvalue="On")
check.deselect()
check.pack()

Button(root, text="Show selection", command=show).pack()

root.mainloop()
