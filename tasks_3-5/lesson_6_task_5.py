"""
**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было
задать имя обоих исходных файлов и имя выходного файла. Проверить работу скрипта.
"""
# исходил из того, что имя файла задается вместе с расширением, как это обычно бывает
# можно было конечно сделать задание только имени, а расширение уже зашить в скрипт...
# удобный вызов
# python lesson_6_task_5.py users.csv hobby.csv users_hobby_out.txt
# можно было бы налепить всяких проверок

import csv
from sys import argv


def users_hobby(users_file, hobby_file, out_file):
    try:
        with open(users_file, 'r', encoding='utf-8') as f_users:
            try:
                with open(hobby_file, 'r', encoding='utf-8') as f_hobby:
                    users_lines_count = sum(1 for _ in f_users)
                    hobbies_lines_count = sum(1 for _ in f_hobby)

                    if users_lines_count < hobbies_lines_count:
                        return 1

                    f_users.seek(0)
                    f_hobby.seek(0)
                    line_users = f_users.readline().strip('\n')
                    line_hobby = f_hobby.readline().strip('\n')

                    # что нибудь с невозвожностью создать или писать в файл из-за прав
                    try:
                        with open(out_file, 'w+') as txt:
                            while line_users:
                                # writer = csv.writer(txt, delimiter='\n', escapechar='\\')
                                writer = csv.writer(txt, delimiter='\n')
                                writer.writerow([f'{line_users}: {line_hobby}'])

                                line_users = f_users.readline().strip('\n')
                                line_hobby = f_hobby.readline().strip('\n')
                    except Exception as e:
                        txt_msg = f'Произошло необработанное исключение: {e}'
                        return txt_msg
                    else:
                        txt_msg = f'Операция успешно завершена. Создан файл {out_file}.'
                        return txt_msg
            except FileNotFoundError:
                txt_msg = f'Нет такого файла {hobby_file}. Возможно вам подойдет hobby.csv.'
                return txt_msg
            except Exception as e:
                txt_msg = f'Произошло необработанное исключение: {e}'
                return txt_msg
    except FileNotFoundError:
        txt_msg = f'Нет такого файла {users_file}. Возможно вам подойдет users.csv.'
        return txt_msg
    # меня отругали, что я так делаю, но я все равно так сделаю
    # потому что не могу углубиться сейчас в др возможные исключения и просто обобщу
    except Exception as e:
        txt_msg = f'Произошло необработанное исключение: {e}'
        return txt_msg


argv_real_len = len(argv) - 1

if argv_real_len == 3:
    my_users_file = argv[1]
    my_hobby_file = argv[2]
    my_out_file = argv[3]
    print(users_hobby(my_users_file, my_hobby_file, my_out_file))
else:
    print(f'Скрипт ожидает 3 параметра в формате [file_name.file_extension]: '
          f'1) файл пользователей, '
          f'2) файл хобби, '
          f'3) результирующий файл')
