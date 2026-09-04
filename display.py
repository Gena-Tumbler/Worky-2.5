from tkinter import *
from PIL import Image, ImageTk
import os
import data_base as wdb
import time
import datetime




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
        status = 1

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
        indication = Label(fone_label, text='STOP', fg='red', bg='black', font=('Roboto Bold', 20))
        indication.place(x=3, y=130)

        self.window.mainloop()



class ButtonCommand(Window):
    """
    Данный класс отвечает за выполнение команд взависимости от нажимаемых кнопок
    """
    @staticmethod
    def command_button_start_status:
        """
        Изменения статуса выполнения после нажатия кнопки start
        """
        Window.status = 0

    @staticmethod
    def command_button_start:
        """
        Команда start отвечает за выполнение программы
        """
        while True:
            Window.indication.configure(text='STOP', fg='red')
            counter_data =wdb.Counter('Shock', 0, 0)
            counter = counter_data.download(1)
            counter_data.close()
            Login, counter_dst, counter_odo = func.repac_download_counter(counter)
            counter_odo = func.integer_to_string(counter_odo, 8)
            counter_dst = func.integer_to_string(counter_dst, 5)
            Window.counter_odo_label.configure(text=counter_odo[0:6])
            Window.counter_dst_label.configure(text=counter_dst[0:3])
            Window.counter_dst_float_label.configure(text=counter_dst[3])
            int_odo = func.string_to_integer(counter_odo)
            int_dst = func.string_to_integer(counter_dst)
            Window.Login_label.configure(text=Login)
            while Window.status == 0:
                Window.indication.configure(text='DRIVE', fg='green')
                Window.Login_lagel.configure(text=Login)
                int_odo += 1
                int_dst += 1
                int_odo = func.big_number(int_odo, 100000000)
                int_dst = func.big_number(int_dst, 100000)
                str_odo = func.integer_to_string(int_odo, 8)
                str_dst = func.integer_to_string(int_dst, 5)
                Window.counter_odo_label.configure(text=str_odo[0:6])
                Window.counter_dst_label.configure(text=str_dst[0:3])
                Window.counter_dst_float_label.configure(text=str_dst[3])
                counter_data_up = wdb.Counter(Window.Login, int_dst, int_odo)
                counter_data_up.update()
                counter_data_up.close()
                time.sleep(1)

    @staticmethod
    def command_button_stop:
        """
        Команда stop отвечает за остановку выполнения программы
        """


        




