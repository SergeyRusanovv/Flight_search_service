from services.checkings import (
    DIGIT_FOR_MINUTES,
    DIGIT_FOR_HOUR_SECOND_LETTER,
    DIGIT_FOR_HOUR_FIRST_LETTER,
    DIGIT_FOR_CHECKS,
    SYMBOLS_NOT_IN_STRING
)


def check_flight_number(string: str, amount_symbols: int) -> bool:
    """
    Функция для проверки номера рейса
    :param string: номер рейса для проверки
    :param amount_symbols: количество символов в строке
    :return: True если символы в строке цифры и длина строки равна 4 или False
    """
    counter: int = 0
    for letter in string:
        counter += 1
        if letter not in DIGIT_FOR_CHECKS:
            return False
    if counter == amount_symbols:
        return True
    return False


def check_formate_date(day: str, month: str, year: str) -> bool:
    """
    Функция для проверки формата даты
    :param day: день
    :param month: месяц
    :param year: год
    :return: True если формат даты верный, иначе False
    """
    day, month, year = int(day), int(month), int(year)
    if day > 31:
        return False
    if month > 12:
        return False
    if year < 2020 or year > 2023:
        return False
    if month == 1 and day > 31\
            or month == 3 and day > 31\
            or month == 5 and day > 31\
            or month == 7 and day > 31\
            or month == 8 and day > 31\
            or month == 10 and day > 31\
            or month == 12 and day > 31:
        return False
    if month == 4 and day > 30\
            or month == 6 and day > 30\
            or month == 9 and day > 30\
            or month == 11 and day > 30:
        return False
    if month == 2 and day > 28:
        return False
    return True


def check_departure_date(string: str, amount_symbols: int) -> bool:
    """
    Функция дял проверки даты вылета
    :param string: дата вылета
    :param amount_symbols: количество символов в строке
    :return: True если символы в строке цифры, разделены / и длина строки равна 10 или False
    """
    counter: int = 0
    day: str = ""
    month: str = ""
    year: str = ""
    for letter in string:
        counter += 1
        if 0 < counter < 3:
            day += letter
        elif 3 < counter < 6:
            month += letter
        elif counter > 6:
            year += letter
        if letter == "/" and counter == 3 \
                or letter == "/" and counter == 6:
            continue
        if letter not in DIGIT_FOR_CHECKS:
            return False
    if counter == amount_symbols and check_formate_date(day=day, month=month, year=year):
        return True
    return False


def check_time(string: str, amount_symbols: int, check_symbol: str) -> bool:
    """
    Функция для проверки времени вылета и времени полета
    :param string: время вылета или перелета
    :param amount_symbols: количество символов в строке
    :param check_symbol: символ который обязательно должны разделять строку
    :return: True если символы в строке цифры, разделены заданным символом и длина строки равна 5 или False
    """
    counter: int = 0
    for letter in string:
        counter += 1
        if letter == check_symbol and counter == 3:
            continue
        if letter not in DIGIT_FOR_CHECKS:
            return False
        if counter == 1 and letter not in DIGIT_FOR_HOUR_FIRST_LETTER:
            return False
        if string[0] == "2" \
                and counter == 2 \
                and letter not in DIGIT_FOR_HOUR_SECOND_LETTER:
            return False
        if counter == 4 \
                and letter not in DIGIT_FOR_MINUTES:
            return False
    if counter == amount_symbols:
        return True
    return False


def check_airport_code(string: str, amount_symbols: int) -> bool:
    """
    Функция для проверки номера аэропорта
    :param string: номер аэропорта
    :param amount_symbols: количество символов в номере
    :return: True если длина строки 3 и в строке нет посторонних символов или False
    """
    counter: int = 0
    for letter in string:
        counter += 1
        if letter in SYMBOLS_NOT_IN_STRING:
            return False
    if counter == amount_symbols:
        return True
    return False


def check_airfare(price: str) -> bool:
    """
    Функция для проверки цены перелета
    :param price: цена перелета
    :return: True если символы в строке цифры и разделитель один
    """
    counter: int = 0
    amount_dots: int = 0
    flag: int = 0
    for digit in price:
        counter += 1
        if digit == '.' \
                and counter > 1 \
                and amount_dots == 0:
            flag = counter
            amount_dots += 1
            continue
        if digit not in DIGIT_FOR_CHECKS:
            return False
    if counter - flag == 2:
        return True
    return False
