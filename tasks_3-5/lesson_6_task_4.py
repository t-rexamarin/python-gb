"""
*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
(разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
Только теперь не нужно создавать словарь с данными.
Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt).
Хобби пишем через двоеточие и пробел после ФИО:
    Иванов,Иван,Иванович: скалолазание,охота
    Петров,Петр,Петрович: горные лыжи
"""
# вышло так, что я обложил всякими проверками 5 задание
# а потом вернулся посмотреть, что я делал тут, но уже решил сосредоточится на проверке
# и не стал вносить правки тут, было уже 12 ночи, не ругайтесь :)

import csv


def users_hobby(users_file, hobby_file, out_file):
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

            with open(out_file, 'w+') as txt:
                while line_users:
                    # writer = csv.writer(txt, delimiter='\n', escapechar='\\')
                    writer = csv.writer(txt, delimiter='\n')
                    writer.writerow([f'{line_users}: {line_hobby}'])

                    line_users = f_users.readline().strip('\n')
                    line_hobby = f_hobby.readline().strip('\n')


my_users_file = 'users.csv'
my_hobby_file = 'hobby.csv'
my_out_file = 'users_hobby.txt'
users_hobbies_are_equal = users_hobby(my_users_file, my_hobby_file, my_out_file)
