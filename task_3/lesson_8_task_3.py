"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...

@type_logger
def calc_cube(x):
   return x ** 3

a = calc_cube(5)
5: <class 'int'>
"""


def type_logger(func):
    def wrapper(*args):
        results = func(*args)
        wrapper_result = []

        for result in results:
            wrapper_result.append(type(result))

        return wrapper_result

    return wrapper


@type_logger
def calc_cube(*args):
    result = []

    for arg in args:
        result.append(arg)

    return result


print(calc_cube('4444', 2, list(), dict()))
