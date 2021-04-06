"""
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
Известно, что при хранении данных используется принцип:
    одна строка — один пользователь, разделитель между значениями — запятая.
Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
    ключи — ФИО, значения — данные о хобби.
Сохранить словарь в файл.
Проверить сохранённые данные.
Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре значение None.
Если наоборот — выходим из скрипта с кодом «1».
При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
"""
# когда в очередной раз пробегался глазами по заданию, понял к чему была фраза
# "При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ."
# надо было читать сразу все, а не построчно. Но увы, не хватит времени поколдовать над этим сейчас

import json


def users_hobby(users_file, hobby_file):
    users_hobbies = {}
    with open(users_file, 'r', encoding='utf-8') as f_users:
        with open(hobby_file, 'r', encoding='utf-8') as f_hobby:
            users_lines_count = sum(1 for _ in f_users)
            hobbies_lines_count = sum(1 for _ in f_hobby)

            if users_lines_count < hobbies_lines_count:
                return 1

            f_users.seek(0)
            f_hobby.seek(0)
            line_users = f_users.readline().strip('\n')
            line_hobby = f_hobby.readline().strip('\n')

            while line_users:
                if len(line_hobby) != 0:
                    users_hobbies[line_users] = line_hobby
                else:
                    users_hobbies[line_users] = None

                line_users = f_users.readline().strip('\n')
                line_hobby = f_hobby.readline().strip('\n')

        # return users_hobbies
    users_file_name, users_file_format = users_file.split('.')
    hobby_file_name, hobby_file_format = hobby_file.split('.')
    result_file = f'{users_file_name}_{hobby_file_name}.json'

    with open(result_file, 'w', encoding='utf-8') as f_json:
        json.dump(users_hobbies, f_json, ensure_ascii=False)

    return result_file


users_hobbies_are_equal = users_hobby('users.csv', 'hobby.csv')
print(f'Юзеров и хобби одинаково. Был создан файл {users_hobbies_are_equal}')

users_more_than_hobbies = users_hobby('users_more.csv', 'hobby.csv')
print(f'\nЮзеров больше чем хобби. Был создан {users_more_than_hobbies}')

users_less_than_hobbies = users_hobby('users.csv', 'hobby_more.csv')
print(f'\nЮзеров меньше чем хобби. Файл не создан. Выход с кодом {users_less_than_hobbies}')
