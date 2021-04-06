"""
*(вместо 6) Добавить возможность редактирования данных при помощи отдельного скрипта:
    передаём ему номер записи и новое значение.
    При этом файл не должен читаться целиком — обязательное требование.
Предусмотреть ситуацию, когда пользователь вводит номер записи, которой не существует.
"""
import pandas as pd
from sys import argv
from helpers import bakery_file, is_digit


def edit_sale(line_number, new_value):
    txt_msg = []

    if is_digit(line_number):
        if is_digit(new_value):
            line_number_original = int(line_number)
            line_number = int(line_number) - 1
        else:
            failure_text = f'Новое значение быть числом. Вы указали {type(new_value)} {new_value}.'
            txt_msg.append(failure_text)
            return txt_msg
    else:
        failure_text = f'Номер строки должен быть числом. Вы указали {type(line_number)} {line_number}.'
        txt_msg.append(failure_text)
        return txt_msg

    try:
        data_frame = pd.read_csv(bakery_file, header=None)
    except FileNotFoundError:
        failure_text = f'Файл {bakery_file} не найден.'
        txt_msg.append(failure_text)
        return txt_msg

    if line_number not in range(len(data_frame.index)):
        failure_text = f'Нет строки с таким номером({line_number_original}). Всего строк {len(data_frame.index)}.'
        txt_msg.append(failure_text)
        return txt_msg
    else:
        previous_value_txt = data_frame.at[line_number, 0]
        # print(type(new_value))
        data_frame.at[line_number, 0] = new_value
        data_frame.to_csv(bakery_file, index=False, header=False)
        new_value_txt = data_frame.at[line_number, 0]

        success_txt = f'Значение в строке {line_number_original} успешно перезаписано, ' \
                      f'{previous_value_txt} -> {new_value_txt}.'
        txt_msg.append(success_txt)

        return txt_msg


real_argv_count = len(argv)-1
if real_argv_count == 2:
    line_num = argv[1]
    new_val = argv[2]

    print(*edit_sale(line_num, new_val))
else:
    print(f'Скрипт ожидает 2 аргумента. Было передано {real_argv_count}.')
