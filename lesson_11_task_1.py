"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату
    в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый — с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod,
    должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_int(cls, date: str):
        day, month, year = date.split('-')
        # правильно ли так ли вызывать статик метод?
        Date.validate_date(day, month, year)

    @staticmethod
    def validate_date(day, month, year):
        day, month, year = int(day), int(month), int(year)
        # TODO: сделать високосный год
        year_start = 1990
        year_stop = 2021
        months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if year in range(year_start, year_stop):
            if month in months.keys():
                if day in range(months[month] + 1):
                    print('yes')
                else:
                    msg = f'День вне допустимого диапазона 1-{months[month]}'
                    raise Exception(msg)
            else:
                msg = f'Месяц вне допустимого диапазона {min(months.keys())}-{max(months.keys())}'
                raise Exception(msg)
        else:
            msg = f'Год вне допустимого диапазона {year_start}-{year_stop}'
            raise Exception(msg)


Date.date_to_int('32-02-2002')
