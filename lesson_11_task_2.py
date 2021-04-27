"""
Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверить его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyZeroDivisionException(Exception):
    # нашел в одном из примеров, но не до конца понимаю, что происходит
    # да, мы дополняем инит родительского класса... но
    # def __init__(self, msg='Zero division error'):
    #     self.msg = msg
    #     super().__init__(self.msg)
    pass


dividends = [1, 2, 3]
divisors = [1, 0, 1]

for dividend, divisor in zip(dividends, divisors):
    try:
        if divisor == 0:
            raise MyZeroDivisionException

        print(dividend / divisor)
    except MyZeroDivisionException:
        print('Поймано мое исключение деления на 0')
