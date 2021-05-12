"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""
# подозреваю, что мог не так понять "кратно 10" и надо делать 100, 1000 и т.д.
# в целом мне очень не нравится, то как у меня это все написано
# выглядит слишком сложно, внутренее чувство говорит мне, что так не должно быть)

import os
from collections import defaultdict

# files_arr = {
#     0: 0,
#     100: 0,
#     1000: 0,
#     10000: 0,
#     100000: 0,
#     1000000: 0
# }
files_arr = defaultdict(int)

for root, dirs, files in os.walk('files'):
    # сюда размеры всех файлов
    files_size = []

    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        files_size.append(file_size)

    keys_set = set()
    keys_set.add(0)
    for i in files_size:
        if i % 10 != 0:
            k = i + (10 - i % 10)
            keys_set.add(k)
        else:
            keys_set.add(i)

    # список ренджей
    list_ranges = [(start, end) for start, end in zip(sorted(keys_set), sorted(keys_set)[1:])]

    for list_range in list_ranges:
        range_start = list_range[0]
        range_stop = list_range[1]

        for file_size in files_size:
            if file_size in range(range_start, range_stop):
                # print(list_range, file_size)
                # files_arr[range_stop] += 1
                files_arr[range_stop] += 1

print(f'Статистика по размерам {dict(files_arr)}')
print(f'Размеры всех файлов {files_size}')
