from tkinter import *

root = Tk()

def click():
    label = Label(root, text="You are a dumb as hehe")
    label.pack()# Puts it on the screen
# The button creation

mButton = Button(root, text="Click to continue", command= click, fg="green")
mButton.pack()
root.mainloop()