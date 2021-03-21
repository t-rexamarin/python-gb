"""
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests.
В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
Рекомендация: выполнить предварительно запрос к API в обычном браузере, посмотреть содержимое ответа.
Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float.
Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
Сильно ли усложняется код функции при этом?
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
В качестве примера выведите курсы доллара и евро.

*(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера. Дата должна быть в виде объекта date.
Подумайте, как извлечь дату из ответа, какой тип данных лучше использовать в ответе функции?

75.18, 2020-09-05
"""
from lxml import etree
from datetime import datetime


def currency_rates(currency):
    """
    @param currency: currency code USD, EUR, GBP, ...
    @type currency: str
    @return: currency rate and currency update date
    @rtype: list[float, date]
    """
    cb_api_url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    parsed = etree.parse(cb_api_url)
    root = parsed.getroot()

    request_date = root.attrib['Date']
    day, month, year = request_date.split('.')
    data_date_format = datetime(day=int(day), month=int(month), year=int(year)).date()

    # почему то мне не очень нравится эта реализация
    result = None
    # нужно только для избежание ошибки referenced before assignment в проверочном принте
    # currency_rate = None

    for elem in root.findall('Valute'):
        if elem.find('CharCode').text == currency.upper():
            currency_value = elem.find('Value').text
            currency_rate = float(currency_value.replace(',', '.'))
            # сначала возвращал строку, пока не опомнился, что нужны float и date
            # result = f'{currency_rate}, {data_date_format}'
            result = [currency_rate, data_date_format]
            break
        else:
            result = [None, data_date_format]

    # print(type(currency_rate))
    # print(type(data_date_format))
    return result


currency_arr = ['USD', 'eur', 'BRL', 'XXX']
for i in currency_arr:
    print(f'{i}', *currency_rates(i))
