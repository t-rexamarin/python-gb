"""
*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
...
Примечание:
структуру файла config.yaml придумайте сами, его можно создать в любом текстовом
    редакторе «руками» (не программно);
предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""

# def line_trimmer(line):
#     if line.endswith(':'):
#         dir_list[line] = None


def line_formatter(line_f):
    if isinstance(line_f, str):
        new_line = line_f.replace(' ', '')\
            .replace(':', '')\
            .replace('-', '')
        # line_f.strip(' :')
        # line_f.strip(':')

        # print(line_f)
        return new_line
    else:
        print('Not str')


# все что с : это ключи, остальное вложенное
with open('config.yaml', 'r', encoding='utf-8') as f:
    dir_list = {}
    line = f.readline().strip('\n')
    if line.endswith(':'):
        formatted_line = line_formatter(line)
        dir_list[formatted_line] = None
    while line:
        line = f.readline().strip('\n')
        if line.endswith(':'):
            formatted_line = line_formatter(line)
            dir_list[formatted_line] = None

    print(dir_list)
