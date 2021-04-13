"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции
и выбрасывать исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

 a = calc_cube(5)
125
 a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5
"""
# сдаю пока как заглушку
# надо с этим разюираться

# from functools import wraps


# def val_checker(arg):
#     def _val_checker(func):
#         # def wrapper(x_from_calc):
#         def wrapper(*args):
#             # result = func(x_from_calc)
#             result = func(*args)
#             anon_func = arg(result)
#
#             for my_arg in args:
#                 if anon_func is not True:
#                     # msg = f'wrong val {x_from_calc}'
#                     msg = f'wrong val {my_arg}'
#                     raise ValueError(msg)
#                 else:
#                     return result
#
#         return wrapper
#
#     return _val_checker

# lambda calc_cube(x): calc_cube(x) > 0
def val_checker(arg):
    def _val_checker(func):
        def wrapper(*args):
            result = func(*args)
            anon_func = arg(result)

            for my_arg in args:
                if anon_func is not True:
                    msg = f'wrong val {my_arg}'
                    raise ValueError(msg)
                else:
                    return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(-5)
print(a)
