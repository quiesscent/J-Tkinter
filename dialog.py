from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
""" The code is used to open a file then displays it on the root window after selecting the file.
    This is an implementation of the filedialog in python tkinter module 
    """
root = Tk()
root.title("Opening files")


def openfile():
    global image
    root.filename = filedialog.askopenfilename(initialdir="/home", title="select an image", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    image = ImageTk.PhotoImage(Image.open(root.filename))
    Label(root, image=image).pack()


Button(root, text="display a file", command=openfile).pack()
root.mainloop()
