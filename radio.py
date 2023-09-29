from tkinter import *
from PIL import *

root = Tk()
root.title("More 'Bout Me")
r = IntVar()
r.set("0")
fav = StringVar()
fav.set("Music")
def clicked(val):
    label = Label(frame, text=r.get())
    label.grid(row=1, column=2)
def favs(val):
    label = Label(frame2, text=fav.get())
    label.grid(row=1, column=2)

favorites = [
    ("Cooking", "Cooking"),
    ("Drawing", "Drawing"),
    ("Music", "Music")
]

frame = LabelFrame(root, text="Hobbies")
frame2 = LabelFrame(root, text="Favorites")
Radiobutton(frame, text="Basketball", variable=r, value=1, command=lambda: clicked(r.get())).grid(row=0, column=1)
Radiobutton(frame, text="Hockey", variable=r, value=2, command=lambda: clicked(r.get())).grid(row=0, column=2)
Radiobutton(frame, text="Fighting", variable=r, value=3, command=lambda: clicked(r.get())).grid(row=0, column=3)
label = Label(frame, text=r.get())
label2 = Label(frame2, text=fav.get())
Radiobutton(frame2, text="Cooking", variable=fav, value="Cooking", command=lambda: favs(fav.get())).grid(row=0, column=1)
Radiobutton(frame2, text="Music", variable=fav, value="Music", command=lambda: favs(fav.get())).grid(row=0, column=2)
Radiobutton(frame2, text="Drawing", variable=fav, value="Drawing", command=lambda: favs(fav.get())).grid(row=0, column=3)
label.grid(row=1, column=2)
label2.grid(row=1, column=2)
frame.grid(row=1, column=0)
frame2.grid(row=2, column=0)
root.mainloop()