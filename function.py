"""
Функции для работы приложения Воркометр
"""

def integer_to_string(counter, number):
    """
    Функция записи числа в формате текста с нужным количеством знаков
    """
    counter = str(counter)
    testing_counter = len(counter)
    if testing_counter < number:
        need_number = number - testing_counter
        new_counter = '0' * need_number + counter
        return new_counter
    elif testing_counter == number:
        new_counter = counter
        return new_counter

def string_to_integer(counter):
    """
    Функция записи текстового числа в формате числовом
    """
    new_counter = int(counter)
    return new_counter

def repac_download_counter(pack_counter):
    """
    Функция распаковки загруженных данных
    """
    try:
        Login, counter_dst, counter_odo = pack_counter[0][1], pack_counter[0][2], pack_counter[0][3]
        return Login, counter_dst, counter_odo
    except IndexError: #Если основная запись в бд повредиться
        return 'Error', 0, 0

def big_number(counter, n):
    if counter == n:
        counter = 0
        return counter
    else:
        return counter

