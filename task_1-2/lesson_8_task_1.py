"""
Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения
извлекает имя пользователя и почтовый домен из email адреса и возвращает их в виде словаря.
Если адрес не валиден, выбросить исключение ValueError. Пример:
    email_parse('someone@geekbrains.ru')
{'username': 'someone', 'domain': 'geekbrains.ru'}
    email_parse('someone@geekbrainsru')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  ...
    raise ValueError(msg)
ValueError: wrong email: someone@geekbrainsru
"""
import re


def email_parse(email):
    reg_ex = re.compile(r'^([\w.-]+)@{1}(\w+\.\w+)$')

    if reg_ex.findall(email):
        results = reg_ex.findall(email)
        name = results[0][0]
        domain = results[0][1]
        result = {'username': name, 'domain': domain}

        return result
    else:
        msg = f'wrong email: {email}'
        raise ValueError(msg)

email_arr = [
    'someone@geekbrains.ru',
    '  someone@geekbrains.ru  ',
    'som eone@geekbrains.ru',
    'someone@geekbrainsru',
    'someonegeekbrains.ru',
    'somE..one@geekbrains.ru.ru',
    'somE..one@geekbrains.ru',
    'som.eone@geekbrains.ru',
    'som_eone@geekbrains.ru',
    'som1eone@geekb1rains.ru1',
    'som-1eone@geekb1rains.ru1',
    'someone@geekb1@rains.ru1'
]

for email_item in email_arr:
    try:
        print(email_parse(email_item))
    except ValueError as e:
        print(e)
