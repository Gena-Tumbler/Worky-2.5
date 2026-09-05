import display
from tkinter import *
import data_base as wdb
import threading

"""
Основное приложение
"""

Login = 'Shock'
counter_dst = 12345
counter_odo = 12345678


worky_display = display.Window()
button_aplication = display.Buttons()
button_aplication.button_start()
button_aplication.button_stop()
button_aplication.button_null()
button_aplication.button_exit()
button_aplication.button_settup()



startproces = threading.Thread(target=display.ButtonCommand.command_button_start)
startproces.start()

display.MenuSettings.create_menu()

worky_display.window.mainloop()