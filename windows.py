from tkinter import *
from PIL import ImageTk, Image
"""This is a python code that generates a single other window that displays our secret image"""
root = Tk()
root.title("Many windows")


def open():
    global m_image
    top = Toplevel()
    top.title("My Secret Image")
    m_image = ImageTk.PhotoImage(Image.open("img/1.jpeg"))
    Label(top, image=m_image).pack()



button = Button(root, text="Click to View the secret image", command=open).pack()
root.mainloop()
