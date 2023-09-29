from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("My Message box")


def pop():
    # messagebox takes the title and the message as the arguments
    # as shown the "this is my pop up is a tite" while the message is "Shoot"
    response = messagebox.askyesno("This is my pop up", "Shooooooot")
    if response == 1:
        Label(root, text='yes').pack()
    # Returns True
    else:
        Label(root, text='No').pack()
    pass


Button(root, text="show", command=pop).pack()

root.mainloop()
