from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Framed")

frame = LabelFrame(root, text='framed huh', padx=50, pady=50)
frame.pack(padx= 10, pady=10)
click = Button(frame, text='inside my frame')
exit = Button(frame, text="Exit", command=root.quit)
click.grid(row=0, column=1)
exit.grid(row=2, column=1)



root.mainloop()