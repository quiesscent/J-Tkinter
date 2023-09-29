from tkinter import *

root = Tk()

label = Label(root,text="Enter your name: ")
## E creates the entry field
e = Entry(root, width=30, bg="grey")
## Positions the entry field
e.grid(row=1,column=1)
#e.insert(0,"Enter your name")

##positions the text
label.grid(row=1,column=0)

    """fuction to call when button clicks
    """
def click():
    label = Label(root, text="Heyyy " + e.get())
    label.grid(row=3, column=1)# Puts it on the screen
# The button creation

mButton = Button(root, text="confirm", command= click, fg="green")
mButton.grid(row=2, column=1)
root.mainloop()