"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке.
Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
"""
import sys
# будет ругаться пока закоменчена 16 строка
import random
import time

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# src = [x for x in range(10000)]
# random.shuffle(src)
print(f'Исходный массив: {src}')

start = time.perf_counter()
# топорно? стоит ли именно так игнорить первый элемент? Первый так или иначе не попадет в сравнение
result = [x for x in src[1:] if src[src.index(x)] > src[src.index(x)-1]]
# my_gen = [x for x in src if next(src)]
finish = time.perf_counter()
print(f'Фактический результат: {result}')
print(f'time {finish - start}')
print(f'Memory {sys.getsizeof(result)}')

# по примеру из чата, реализация красивая, жаль сам не додумался
# фиксирую как напоминание себе
# result = [second for first, second in zip(src, src[1:]) if first < second]
