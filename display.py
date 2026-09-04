from tkinter import *
from PIL import Image, ImageTk
import os

class Window:
    """
    Функция отрисовывающая графику приложения
    """
    def __init__(self):
        self.window = Tk()
        base = os.path.dirname(__file__)
        path = os.path.join(base, "template", "media", "image", "worky.jpg")
        self.img = ImageTk.PhotoImage(Image.open(path))
        self.label = Label(self.window, image=self.img)
        self.label.pack()
        self.window.geometry("380x188")
        self.window.title('Воркометр 2.5')

        # Временные файлы
        Login = 'Гена Тумблер'
        counter_dst = '12345'
        counter_odo = '12345678'

        Login_txt = Login
        counter_dst_txt = counter_dst
        counter_odo_txt = counter_odo

        fone_label = Label(self.window, image=self.img)
        fone_label.place(x=0, y=0)
        Login_label = Label(fone_label, text=Login_txt, font=('Roboto Bold', 12))
        Login_label.place(x=5, y=150)
        counter_dst_label = Label(fone_label, text=counter_dst_txt[0:3], font=('Roboto Bold', 12))
        counter_dst_label.place(x=166, y=67)
        counter_dst_float_label = Label(fone_label, text=counter_dst_txt[3], font=('Roboto Bold', 12))
        counter_dst_float_label.place(x=194, y=67)
        counter_dst_float_label.configure(fg='red')
        counter_odo_label = Label(fone_label, text=counter_odo_txt[0:6], font=('Roboto Bold', 13))
        counter_odo_label.place(x=156, y=102)

        self.window.mainloop()



