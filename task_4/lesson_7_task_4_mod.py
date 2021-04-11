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

import os

files_arr = {
    0: 0,
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0,
    1000000: 0
}

for root, dirs, files in os.walk('files', topdown=True):
    files_size = []
    list_ranges = [(start, end) for start, end in zip(list(files_arr), list(files_arr)[1:])]

    for file in files:
        file_size = os.stat(os.path.join(root, file)).st_size
        files_size.append(file_size)

        for list_range in list_ranges:
            range_start = list_range[0]
            range_stop = list_range[1]

            if file_size in range(range_start, range_stop):
                # print(list_range, file_size)
                files_arr[range_stop] += 1

    # print(max(files_size))
    files_arr.pop(0)



        # for k, v in enumerate(keys_arr):
        #     if file_size > keys_arr[k] and file_size < keys_arr[k+1]:

    # print(keys_arr)

        # не больше к, но больше к-1
        # dict_to_list = list(enumerate(files_arr))
        # for k, v in dict_to_list[1:]:
        #     if file_size < dict_to_list[k] and file_size > dict_to_list[k-1]:
        #         print(v)
        #         # print(f'size > {k}')
        #         files_arr[v] += 1

print(files_arr)
print(files_size)
