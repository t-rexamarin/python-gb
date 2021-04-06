"""
Для чтения данных реализовать в командной строке следующую логику:
    просто запуск скрипта — выводить все записи;
    запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
    запуск скрипта с двумя числами — выводить записи, начиная с номера,
        равного первому числу, по номер, равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
"""
# наверно, решение было бы более красивым, если работать с байтами
# но т.к. длинна строки в исходном файле не фиксирована, сделал как сделал
# да, на вебинаре говорилось, что можно условится длинной в 20 символов
# но я решил отказаться от такой условности
# как итог, получилось то, что получилось

import csv
from sys import argv
from sys import getsizeof
from helpers import bakery_file, indexes_check

# file_size = getsizeof(bakery_file)
# print(file_size)


def show_sales(file, start_from=None, stop_at=None):
    indexes = indexes_check(start_from, stop_at)

    if type(indexes) == list:
        return indexes
    else:
        start_from = indexes[0]
        stop_at = indexes[1]

    with open(file, encoding='utf-8') as f:
        file_reader = csv.reader(f)
        # rows_count = sum(1 for _ in file_reader)

        # восстанавливал в спешке, т.к. когда чистил коменты видимо стер этот блок
        # if start_from is not None and start_from > rows_count:
        #     txt_msg = [f'Запрошены результаты с {start_from} строки. Всего строк в файле: {rows_count}.']
        #     return txt_msg
        # print(type(f))
        data = [line[0].strip('\n') for line in list(file_reader)[start_from:stop_at]]
        # print(getsizeof(file_reader))
    return data


real_argv_count = len(argv) - 1
if real_argv_count == 0:
    print(*show_sales(bakery_file), sep='\n')
elif real_argv_count == 1:
    start_arg = argv[1]
    print(*show_sales(bakery_file, start_from=start_arg), sep='\n')
elif real_argv_count == 2:
    start_arg = argv[1]
    stop_arg = argv[2]
    print(*show_sales(bakery_file, start_from=start_arg, stop_at=stop_arg), sep='\n')
else:
    print(f'Передано аргументов скрипту: {real_argv_count}. Ожидается не больше 2.')
