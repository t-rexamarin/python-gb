"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
"""

import os
import shutil
import re

project_dir = 'my_project'

files_list = []
for root, dirs, files in os.walk('my_project', topdown=True):
    for file in files:
        if file.endswith('.html'):
            files_list.append(f'{root}/{file}')

for file in files_list:
    reg_ex = re.compile(r'/templates/(?P<folder>\w+)/(?P<file>\w+\.html)')
    result = reg_ex.search(file)

    my_file = result.group('file')
    my_folder = result.group('folder')

    templates_folder = 'templates'
    new_templates_dir = os.path.join(project_dir, templates_folder, my_folder)
    if not os.path.exists(new_templates_dir):
        os.makedirs(new_templates_dir)

    shutil.move(file, new_templates_dir)
