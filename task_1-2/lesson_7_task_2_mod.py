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

        return new_line
    else:
        print('Not str')

#
# def project_maker(n_project, n_line):
#     if line.endswith(':'):
#         n_project[n_line] = []
#     else:


# все что с : это ключи, остальное вложенное
with open('config.yaml', 'r', encoding='utf-8') as f:
    lines = []
    line = f.readline().strip('\n').replace(':', '')
    lines.append(line)
    # line = f.readline().strip('\n').replace(':', '')
    # print(line)
    # project[line] = {}
    # previous_line_indent = 0
    while line:
        line = f.readline().strip('\n').replace('-', '')
        lines.append(line)

        # print(line)
        # print(line_indent)

    project = {}
    root = None
    for key, line in enumerate(lines[:-1]):
        # print(line)

        if key == 0:
            project[line] = []
            root = line
        else:
            # кол-во спейсов предыдущей линии
            previous_line = list(lines)[key - 1]
            previous_line_rm_spaces = previous_line.lstrip(' ')
            previous_line_indent = len(previous_line) - len(previous_line_rm_spaces)

            # кол-во спейсов текущей линии
            current_line = list(lines)[key]
            current_line_rm_spaces = current_line.lstrip(' ')
            current_line_indent = len(current_line) - len(current_line_rm_spaces)

            # если длинна как у текущего, то надо добавить в текущий дикт
            if current_line_indent == previous_line_indent:
                # last_key = list(project[root])[0]
                # project[root] = {line}
                # print(last_key)
                pass
            # если длинна текущего больше, то проваливаемся в папку
            elif current_line_indent > previous_line_indent:
                if line.endswith(':'):
                # last_key = list(project)[-1]
                # print(project.get(last_key))
                    new_dict = dict()
                    new_dict[line] = {}
                    project[root].append(dict(line))
                else:
                    project[root].append(line)
            # если длинна меньше, то
            elif current_line_indent < previous_line_indent:
                pass

            # if line.endswith(':'):
            #     rem_leading_spaces = line.lstrip(' ')
            #     line_indent = len(line) - len(rem_leading_spaces)
            #
            #     if line_indent > previous_line_indent:
            #         last_key = list(project)[-1]
            #         project.get(last_key)[line] = {}


    # rem_leading_spaces = line.lstrip(' ')
    # line_indent = len(line) - len(rem_leading_spaces)
    #
    # if line_indent > previous_line_indent:
    #     project[line] = {}
    # previous_line_indent = line_indent

    # print(lines)
    print(project)