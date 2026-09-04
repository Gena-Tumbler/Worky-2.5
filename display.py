from tkinter import *
from PIL import Image, ImageTk
import os
import data_base as wdb
import time
import function as func
import datetime




class Window:
    """
    Функция отрисовывающая графику приложения
    """
    #def __init__(self):
    window = Tk()
    base = os.path.dirname(__file__)
    path = os.path.join(base, "template", "media", "image", "worky.jpg")
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(window, image=img)
    label.pack()
    window.geometry("380x222")
    window.title('Воркометр 2.5')

    # Временные файлы
    Login = 'Гена Тумблер'
    counter_dst = '12345'
    counter_odo = '12345678'
    status = 1

    Login_txt = Login
    counter_dst_txt = counter_dst
    counter_odo_txt = counter_odo

    fone_label = Label(window, image=img)
    fone_label.place(x=0, y=0)
    Login_label = Label(fone_label, text=Login_txt, font=('Roboto Bold', 12))
    Login_label.place(x=5, y=150)
    counter_dst_label = Label(fone_label, text=counter_dst_txt[0:3], font=('Roboto Bold', 12))
    counter_dst_label.place(x=166, y=67)
    counter_dst_float_label = Label(fone_label, text=counter_dst_txt[3], font=('Roboto Bold', 12))
    counter_dst_float_label.place(x=197, y=67)
    counter_dst_float_label.configure(fg='red')
    counter_odo_label = Label(fone_label, text=counter_odo_txt[0:6], font=('Roboto Bold', 13))
    counter_odo_label.place(x=156, y=102)
    indication = Label(fone_label, text='STOP', fg='red', bg='black', font=('Roboto Bold', 20))
    indication.place(x=3, y=100)


class ButtonCommand(Window):
    """
    Данный класс отвечает за выполнение команд взависимости от нажимаемых кнопок
    """
    @staticmethod
    def command_button_start_status():
        """
        Изменения статуса выполнения после нажатия кнопки start
        """
        Window.status = 0

    @staticmethod
    def command_button_start():
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
                Window.Login_label.configure(text=Login)
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
                counter_data_up.update(1)
                counter_data_up.close()
                time.sleep(1)

    @staticmethod
    def command_button_stop():
        """
        Команда stop отвечает за остановку выполнения программы
        """
        Window.status = 1
        Window.indication.configure(text='STOP', fg='red')
        counter_data = wdb.Counter('Shock', 0, 0)
        counter = counter_data.download(1)
        counter_data.close()
        Login, counter_dst, counter_odo = func.repac_download_counter(counter)
        counter_data_reserve = wdb.Counter(Login, counter_dst, counter_odo)
        counter_data_reserve.update(2)
        counter_data_reserve.close()

    @staticmethod
    def command_button_null():
        """
        Кнопка обнуления верхнего счетчика (суточного)
        """
        counter_data = wdb.Counter('Shock', 0, 0)
        counter = counter_data.download(1)
        counter_data.close()
        Login, counter_dst, counter_odo = func.repac_download_counter(counter)
        counter_data_new = wdb.Counter(Login, 0, counter_odo)
        counter_data_new.update(1)
        counter_data.close()

    @staticmethod
    def reserve_load():
        """
        Загрузка резервной копии
        """
        counter_data = wdb.Counter('Shock', 0, 0)
        counter = counter_data.download(2)
        counter_data.close()
        Login, counter_dst, counter_odo = func.repac_download_counter(counter)
        counter_data_new = wdb.Counter(Login, counter_dst, counter_odo)
        counter_data_new.save(1)
        counter_data_new.close()

    @staticmethod
    def enter_user_name():
        """
        Ввод имени пользователя
        """
        user_name_txt = Entry(Window.window, width=10)
        user_name_txt.place(x=10, y=10)

        def get_user_input():
            Login = user_name_txt.get()
            print(Login, 'ustxtgetLogin')
            user_name_txt.place_forget()
            submit_button.place_forget()
            counter = wdb.Counter(Login, 0, 0)
            print(counter, 'counternext')
            counter.save(1)
            counter.close()
        submit_button = Button(Window.window, text='Submit', command=get_user_input)
        submit_button.place(x=10, y=40)

    @staticmethod
    def clickexit():
        """
        Выход из приложения
        """
        Window.window.destroy()


class Buttons(Window):
    """
    Отображение кнопок в окне приложения и назначение им команд
    """
    @staticmethod
    def button_start():
        button_start = Button(
            Window.fone_label, text='D', fg='green', font=('Roboto Bold', 16),
            command=ButtonCommand.command_button_start_status
        )
        button_start.place(x=330, y=10)

    @staticmethod
    def button_stop():
        button_stop = Button(
            Window.fone_label, text='S', fg='red', font=('Roboto Bold', 16),
            command=ButtonCommand.command_button_stop
        )
        button_stop.place(x=330, y=60)

    @staticmethod
    def button_null():
        button_null = Button(
            Window.fone_label, text='0', fg='black', font=('Roboto Bold', 16),
            command=ButtonCommand.command_button_null
        )
        button_null.place(x=330, y=110)


class MenuSettings(Window):
    print('menu settings1')
    @staticmethod
    def create_menu():
        print('menu settings2')
        menu = Menu(Window.window)
        new_item = Menu(menu, tearoff=0)
        new_item.add_command(label='Drive', command=ButtonCommand.command_button_start_status)
        new_item.add_command(label='Stop', command=ButtonCommand.command_button_stop)
        new_item.add_command(label='Null', command=ButtonCommand.command_button_null)
        new_item.add_command(label='Reserve Load', command=ButtonCommand.reserve_load)
        new_item.add_command(label='Enter Name', command=ButtonCommand.enter_user_name)
        new_item.add_command(label='Exit', command=ButtonCommand.clickexit)
        menu.add_cascade(label='file', menu=new_item)
        Window.window.config(menu=menu)
        print(Window.window.config('menu'))

    """
    Класс меню приложения
    """
#    menu = Menu(Window.window)
#    new_item = Menu(menu, tearoff=0)
#    new_item.add_command(label='Drive', command=ButtonCommand.command_button_start_status)
#    new_item.add_command(label='Stop', command=ButtonCommand.command_button_stop)
#    new_item.add_command(label='Null', command=ButtonCommand.command_button_null)
#    new_item.add_command(label='Reserve Load', command=ButtonCommand.reserve_load)
#    new_item.add_command(label='Enter Name', command=ButtonCommand.enter_user_name)
#    new_item.add_command(label='Exit', command=ButtonCommand.clickexit)
#    menu.add_cascade(label='file', menu=new_item)
#    Window.window.config(menu=menu)
        




