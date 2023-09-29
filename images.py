from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Jussie")
#root.iconbitmap('./home/ci-pher/cicada/Tkinter/download.ico')
quit = Button(root, text="Exit", command=root.quit)
image = ImageTk.PhotoImage(Image.open("download.png"))
label = Label(image=image)
label.pack()
quit.pack()

root.mainloop()