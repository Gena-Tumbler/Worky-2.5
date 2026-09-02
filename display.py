from tkinter import *
from PIL import Image, ImageTk
import os

class Window:
    def __init__(self):
        self.window = Tk()
        base = os.path.dirname(__file__)
        path = os.path.join(base, "template", "media", "image", "worky.jpg")
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.label = Label(self.window, image=self.img)
        self.label.pack()
        self.window.geometry("380x188")
        self.window.title('Воркометр 2.5')
        self.window.mainloop()