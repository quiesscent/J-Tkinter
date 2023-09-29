from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Sliders")
vertical = Scale(root, from_=0, to=200)
vertical.pack()
hor = Scale(root, from_=0, to=200, orient=HORIZONTAL)
hor.pack()
def change():
    Label(root, text=hor.get()).pack()
    root.geometry(str(hor.get()) + "x400")


Button(root, text="resize", command=change).pack()

root.mainloop()
