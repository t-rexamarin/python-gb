"""
lesson_4_task_4
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего задания.
Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов функции
currency_rates(). Убедиться, что ничего лишнего не происходит.
"""
import utils

currency = ['AUD', 'USD', 'GBP', 'BRL', 'KGS', 'XXX']

print(f'{len(currency)} раз вызываю метод currency_rates')
for i in currency:
    print(f'{i}', *utils.currency_rates(i))
