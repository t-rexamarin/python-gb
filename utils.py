"""
lesson_4_task_4
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции
currency_rates(). Убедиться, что ничего лишнего не происходит.
"""
from lxml import etree
from datetime import datetime


def currency_rates(currency):
    cb_api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    parsed = etree.parse(cb_api_url)
    root = parsed.getroot()

    request_date = root.attrib['Date']
    day, month, year = request_date.split('.')
    data_date_format = datetime(day=int(day), month=int(month), year=int(year)).date()

    # почему то мне не очень нравится эта реализация
    result = None

    for elem in root.findall('Valute'):
        if elem.find('CharCode').text == currency.upper():
            currency_value = elem.find('Value').text
            currency_rate = float(currency_value.replace(',', '.'))
            result = [currency_rate, data_date_format]
            break
        else:
            result = [None, data_date_format]

    return result


if __name__ == '__main__':
    print(*currency_rates('USD'))
    print(*currency_rates('eur'))
    print(*currency_rates('XXX'))
