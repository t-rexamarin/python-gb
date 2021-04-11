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

# main_dir = os.getcwd()

# TODO: сделать через input
main_folder = input('Введите название проекта: ')
sub_folders = ['settings', 'mainapp', 'adminapp', 'authapp']

if not os.path.exists(main_folder):
    try:
        os.mkdir(main_folder)
    except Exception as e:
        print(f'Произошло необработанное исключение: {e}')
    else:
        for sub_folder in sub_folders:
            try:
                os.mkdir(os.path.join(main_folder, sub_folder))
            except Exception as e:
                print(f'Произошло необработанное исключение: {e}')
else:
    print(f'Проект с таким именем - {main_folder} - уже существует')
