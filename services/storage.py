STORAGE: str = ""


def write_data_in_storage(flight_number, departure_date, departure_time, flight_time,
                          departure_airport_IATA_code, arrival_airport_IATA_code, airfare) -> None:
    """Функция для записи данных рейса в хранилище"""
    global STORAGE
    STORAGE += f"{flight_number} {departure_date} {departure_time} " \
               f"{flight_time} {departure_airport_IATA_code} " \
               f"{arrival_airport_IATA_code} {airfare}\n"
    return


def print_all_data() -> None:
    """
    Функция для вывода всех рейсов
    :return: None
    """
    global STORAGE
    if STORAGE == "":
        print("\nВ базе данных нет сохраненных рейсов!")
    counter: int = 0
    new_line: str = ""
    for letter in STORAGE:
        if letter == "\n":
            counter += 1
            print(f"Рейс №{counter}: {new_line}")
            new_line: str = ""
            continue
        new_line += letter
    return


def search_flight(string: str, number: str) -> bool:
    """
    Функция для проверки конкретного рейса в базе данных
    :param string: данные рейса
    :param number: номер рейса
    :return: True если номер рейса находится в строке или False
    """
    counter: int = 0
    number_in_storage: str = ""
    for letter in string:
        counter += 1
        if counter > 4:
            break
        number_in_storage += letter
    if number == number_in_storage:
        return True
    return False


def check_data_base(number: str) -> str:
    """
    Функция для нахождения рейса по его номеру
    :param number: номер рейса
    :return: Данные рейса или сообщение о его отсутствии
    """
    global STORAGE
    if STORAGE == "":
        return "\nСохраненных рейсов нет!"
    new_string: str = ""
    for letter in STORAGE:
        if letter == "\n":
            if search_flight(string=new_string, number=number):
                return f"Данные рейса номер {number}: {new_string}"
            new_string: str = ""
            continue
        new_string += letter
    else:
        return "\nУказанного рейса не найдено!"
