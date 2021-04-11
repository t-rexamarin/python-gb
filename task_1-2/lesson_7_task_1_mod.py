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
import itertools

main_folder = input('Введите название проекта: ')
sub_folders = {
                'settings': 'settings',
                'mainapp': 'mainapp',
                'adminapp': 'adminapp',
                'authapp': 'authapp',
                'some_folder': {
                        'some_sub_folder_1': 'some_sub_folder_1',
                        'some_file': 'some_file.file',
                        'some_sub_folder2': {
                            'some_sub_sub_folder': 'some_sub_sub_folder',
                            'some_file': 'some_file.file'
                        }
                }

            }

paths_config = {main_folder: sub_folders}
# print(paths_config, type(paths_config[main_folder]))


def tree_builder(tree):
    for key, value in tree.items():
        if isinstance(value, dict):
            # print('dict')
            os.mkdir(key)
            tree_builder(value)
        # else:
        #     print('not a dict')


tree_builder(paths_config)

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
