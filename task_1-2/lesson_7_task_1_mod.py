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
import os

main_folder = input('Введите название проекта: ')
sub_folders = [
                'settings',
                'mainapp',
                'adminapp',
                'authapp',
            ]


# TODO: сделать работу с вложенными папками
def tree_builder(main_folder, sub_folders):
    path = [main_folder]
    for key, value in enumerate(sub_folders):
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

# def tree_builder(tree):
#     for key, val in tree.items():
#         print(val, type(val))
#         if isinstance(val, dict):
#             if not os.path.exists(key):
#                 try:
#                     os.mkdir(key)
#                 except Exception as e:
#                     print(f'Произошло необработанное исключение: {e}')


# tree_builder(paths_config)

# for main_dir in paths_config.keys():
#     if not os.path.exists(main_dir):
#         try:
#             os.mkdir(main_dir)
#         except Exception as e:
#             print(f'Произошло необработанное исключение: {e}')
#         else:
#             for sub_folder in list(*paths_config.values()):
#                 try:
#                     os.mkdir(os.path.join(main_dir, sub_folder))
#                 except Exception as e:
#                     print(f'Произошло необработанное исключение: {e}')
#                 # print(sub_folder)
#     else:
#         print(f'Проект с таким именем - {main_dir} - уже существует')
