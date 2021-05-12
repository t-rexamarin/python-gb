"""
Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
# не закончил с ней, хотел поиграться с вложенным словарями

import os

main_folder = input('Введите название проекта: ')
sub_folders = [
                'settings',
                'mainapp',
                'adminapp',
                'authapp',
            ]


# TODO: сделать работу с вложенными папками
def tree_builder(my_main_folder, my_sub_folders):
    path = [my_main_folder]
    for key, value in enumerate(my_sub_folders):
        if isinstance(value, dict):
            pass
            # print(value.values())
            # tree_builder(value.keys(), value.items())
            # # for key_sub, value_sub in enumerate(value):
            # #     path.append(value_sub)
            # #     os.makedirs(os.path.join(*path))
            # #     # position = path.index(value_sub)
            # #     # path.pop(position)
            # #     tree_builder(path)
        else:
            path.append(value)
            os.makedirs(os.path.join(*path))
            position = path.index(value)
            path.pop(position)


tree_builder(main_folder, sub_folders)
