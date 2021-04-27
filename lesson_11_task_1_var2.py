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
import datetime


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def date_to_int(cls, date: str):
        # day, month, year = date.split('-')
        if Date.validate_date(date):

        # print(day, month, year)


    @staticmethod
    def validate_date(date: str):
        date_format = '%d-%m-%Y'

        try:
            datetime.datetime.strptime(date, date_format)
        except ValueError:
            return False

Date.date_to_int('22-12-2002')
