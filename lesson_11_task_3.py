"""
Создать собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
"""


# class NotIntException(Exception):
#     pass

class NotIntException(Exception):
    def __init__(self, string, msg='Вы ввели не число'):
        self.string = string
        self.msg = msg
        super().__init__(self.string)

    def int_check(self):
        try:
            int(self.string)
        except ValueError:
            raise NotIntException(self.msg)


my_list = []
user_input = None


while user_input != "stop":
    user_input = input('Введите число (для остановки введите "stop"): ')
    try:
        my_exception_instance = NotIntException(user_input)
        my_exception_instance.int_check()
    except NotIntException as e:
        print(e)
    else:
        my_list.append(user_input)

    # до того, как я понял, что проверку похоже надо перенести в сам класс
    # try:
    #     try:
    #         user_input_to_int = int(user_input)
    #         my_list.append(user_input_to_int)
    #     except ValueError:
    #         raise NotIntException
    # except NotIntException:
    #     print('Введенное значение не int')


print(my_list)
