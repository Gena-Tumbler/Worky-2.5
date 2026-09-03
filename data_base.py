"""
Worky v-2.5 data base
"""

import sqlite3 as sql


class Counter:
    """
    Класс экземпляра счетчика.
    Сохранение, загрузка, инициация и формат данных
    """
    def __init__(self, Login, counter_dst, counter_odo):
        """
        Инициализация класса Counter
        """
        self.Login = Login
        self.counter_dst = counter_dst
        self.counter_odo = counter_odo
        self.connect_data_base = sql.connect("worky_DataBase.db")
        self.cursor = self.connect_data_base.cursor()
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Login TEXT NOT NULL,
        counter_dst INTEGER,
        counter_odo INTEGER
        )
        ''')

    def save(self, record_id=None):
        """
        функция сохранения данных
        """
        if record_id is None:
            self.cursor.execute(
                'INSERT INTO Users(Login, counter_dst, counter_odo) VALUES (?, ?, ?)',
                (self.Login, self.counter_dst, self.counter_odo)
            )
        else:
            self.cursor.execute(
                'UPDATE Users SET Login = ?, counter_dst = ?, counter_odo = ? WHERE id = ?',
                (self.Login, self.counter_dst, self.counter_odo, record_id)
            )
        self.connect_data_base.commit()

    def download(self, record_id):
        """
        Функция загрузки данных
        """
        self.cursor.execute('SELECT * FROM Users WHERE id = ?', (record_id,))
        counter = self.cursor.fetchall()
        #connect_data_base.commit()
        #connect_bata_base.close()
        return counter

    def update(self, record_id):
        """
        Функция обновления данных
        """
        self.cursor.execute(
            'UPDATE Users SET Login = ?, counter_dst = ?, counter_odo = ? WHERE id = ?',
            (self.Login, self.counter_dst, self.counter_odo, record_id)
        )
        self.connect_data_base.commit()

    def close(self):
        """
        Функция закрытия базы данных
        """
        self.connect_data_base.close()