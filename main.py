from services import messages
from services.check_functions import (
    check_flight_number,
    check_departure_date,
    check_time,
    check_airport_code,
    check_airfare,
)
from services.storage import (
    write_data_in_storage,
    print_all_data,
    check_data_base
    )


def menu() -> None:
    """
    Функция выполняющая весь основной скрипт
    :return: None
    """
    print(messages.HELLO)
    while True:
        print(messages.MENU)
        commands: str = input(messages.INPUT_MENU_ITEM)

        match commands:
            case commands if commands == "1":
                print(messages.INPUT_DATA)
                while True:
                    flight_number: str = input(messages.INPUT_NUMBER).upper()
                    if check_flight_number(string=flight_number, amount_symbols=4):
                        break
                    print(messages.ERROR_DATA)

                while True:
                    departure_date: str = input(messages.INPUT_DATE)
                    if check_departure_date(string=departure_date, amount_symbols=10):
                        break
                    print(messages.ERROR_DATA)

                while True:
                    departure_time: str = input(messages.INPUT_DEPARTURE_TIME)
                    if check_time(string=departure_time, amount_symbols=5, check_symbol=":"):
                        break
                    print(messages.ERROR_DATA)

                while True:
                    flight_time: str = input(messages.INPUT_FLIGHT_TIME)
                    if check_time(string=flight_time, amount_symbols=5, check_symbol="."):
                        break
                    print(messages.ERROR_DATA)

                while True:
                    departure_airport_IATA_code: str = input(messages.INPUT_AIRPORT_DEPARTURE_CODE).upper()
                    if check_airport_code(string=departure_airport_IATA_code, amount_symbols=3):
                        break
                    print(messages.ERROR_DATA)

                while True:
                    arrival_airport_IATA_code: str = input(messages.INPUT_AIRPORT_ARRIVAL_CODE).upper()
                    if check_airport_code(string=departure_airport_IATA_code, amount_symbols=3):
                        break
                    print(messages.ERROR_DATA)

                while True:
                    airfare: str = input(messages.INPUT_AIRFARE)
                    if check_airfare(price=airfare):
                        break
                    print(messages.ERROR_DATA)
                print(f'\nИнформация о рейсе {flight_number} {departure_date} {departure_time} {flight_time}'
                      f' {departure_airport_IATA_code} {arrival_airport_IATA_code} {airfare} сохранена.')
                write_data_in_storage(flight_number=flight_number, departure_date=departure_date, departure_time=departure_time,
                                      flight_time=flight_time, departure_airport_IATA_code=departure_airport_IATA_code,
                                      arrival_airport_IATA_code=arrival_airport_IATA_code, airfare=airfare)

            case commands if commands == '2':
                print_all_data()

            case commands if commands == '3':
                choice_number: str = input(messages.INPUT_SEARCH_FLIGHT).upper()
                print(check_data_base(number=choice_number))

            case commands if commands == '0':
                print(messages.FAREWELL)
                break

            case _:
                print(messages.ERROR_INPUT_MENU)


if __name__ == "__main__":
    menu()
