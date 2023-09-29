from tkinter import *
from PIL import ImageTk, Image
# This programm add a status bar on the application.
# This aid in allowing the user to know in or under which picture he/she is.
root = Tk()
root.title("LITTLE GALLERY")
exit = Button(root, text="exit", command=root.quit)
img1 = ImageTk.PhotoImage(Image.open("img/1.jpeg"))
img2 = ImageTk.PhotoImage(Image.open("img/2.jpeg"))
img3 = ImageTk.PhotoImage(Image.open("img/3.png"))
img4 = ImageTk.PhotoImage(Image.open("img/4.jpeg"))
img5 = ImageTk.PhotoImage(Image.open("img/5.jpeg"))
img6 = ImageTk.PhotoImage(Image.open("img/6.jpeg"))
slide = [img1, img2, img3, img4, img5, img6]

status = Label(root, text="Image 1 of " + str(len(slide)), bd=1, relief=SUNKEN)

def forward(count):
    global label
    global front
    global back
    label.grid_forget()
    label = Label(image=slide[count - 1])
    front = Button(root, text=">>", command=lambda: forward(count + 1))
    back = Button(root, text="<<", command= lambda: backward(count - 1))

    status = Label(root, text="Image " + str(count) + " of " + str(len(slide)), bd=1, relief=SUNKEN)
    if count == 6:
        front = Button(root, text=">>", state= DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    front.grid(row=1, column=1)
    back.grid(row=1, column=0)
    exit.grid(row=1, column=2)
    status.grid(row=2,column=2)

def backward(count):
    global label
    global front
    global back
    label.grid_forget()
    label = Label(image=slide[count - 1])
    front = Button(root, text=">>", command=lambda: forward(count + 1))
    back = Button(root, text="<<", command=lambda: backward(count - 1))

    status = Label(root, text="Image " + str(count) + " of " + str(len(slide)), bd=1, relief=SUNKEN)
    if count == 1:
        back = Button(root, text="<<", state=DISABLED)

    label.grid(row=0, column=0, columnspan=3)
    front.grid(row=1, column=1)
    back.grid(row=1, column=0)
    exit.grid(row=1, column=2)
    status.grid(row=2, column=2)

label = Label(image=img1)
label.grid(row=0, column=0, columnspan=3)
back = Button(root, text="<<", command=lambda:backward, state=DISABLED)
front = Button(root, text=">>", command=lambda: forward(2))

back.grid(row=1, column=0)
front.grid(row=1, column=1)
exit.grid(row=1, column=2)
status.grid(row=2, column=2)

root.mainloop()
