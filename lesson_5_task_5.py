"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать из этих элементов список с сохранением порядка их следования в исходном списке,
например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

"""
import sys
import time

# при нем разница во времени минимальна
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# на этом уже можно увидеть степень профита по скорости
src = [
        2, 2, 2, 7, 23, 99, 99, 1, 44, 44, 3, 2, 10, 7, 4, 66, 11, 2, 7, 7, 7, 7, 23, 1, 44, 44, 3, 101, 2,
        10, 7, 4, 11, 2, 7, 23, 1, 44, 77, 44, 3, 2, 10, 7, 4, 11, 241, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4,
        11, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11
        ]

start = time.perf_counter()
result = [x for x in src if src.count(x) == 1]
finish = time.perf_counter()
print(f'Первый вариант - генератор через count. '
      f'{result} memory {sys.getsizeof(result)}, time {finish - start}')


def my_func(source):
    unique_numbers = []
    tmp = []

    for x in source:
        if x not in tmp:
            unique_numbers.append(x)
        elif x in tmp and x in unique_numbers:
            unique_numbers.remove(x)
        tmp.append(x)
    return unique_numbers


def my_func_set(source):
    unique_numbers = set()
    tmp = set()

    for x in source:
        if x not in tmp:
            unique_numbers.add(x)
        else:
            unique_numbers.discard(x)
        tmp.add(x)
    return unique_numbers


start = time.perf_counter()
my_func_result = my_func(src)
finish = time.perf_counter()
print(f'Второй вариант - цикл с list. '
      f'{my_func_result} memory {sys.getsizeof(my_func_result)}, time {finish - start}')

start = time.perf_counter()
my_func_set_result = my_func_set(src)
finish = time.perf_counter()
print(f'Третий вариант - цикл с set. '
      f'{my_func_result} memory {sys.getsizeof(my_func_set_result)}, time {finish - start}')
