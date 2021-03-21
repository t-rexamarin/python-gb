"""
lesson_4_task_4
*(вместо 4) Доработать скрипт из предыдущего задания:
теперь он должен работать и из консоли. Например:
python task_4_5.py USD
    75.18, 2020-09-05
"""
import utils
from sys import argv

# print(list(map(utils.currency_rates, currency)))
for currency in argv[1:]:
    print(f'{currency}', *utils.currency_rates(currency))
