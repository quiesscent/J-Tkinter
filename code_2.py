from tkinter import *

root = Tk()

label = Label(root, text="My name is Jussie")
label2 = Label(root, text=" I live in Nairobi")

# This shows the grid position in the code display on the screen
label.grid(row=0, column=0)
label2.grid(row=0,column=1)

    """shorter Version of the code
    label = Label(root, text="My name is Jussie").grid(row=0, column=0)
    label2 = Label(root, text=" I live in Nairobi").grid(row=0, column=1)

    """

root.mainloop()