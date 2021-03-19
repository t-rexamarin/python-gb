"""
*(вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов
строки в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
в которых фамилия начинается с соответствующей буквы. Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": ["Петр Алексеев"]
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}

Как поступить, если потребуется сортировка по ключам?

"""


def thesaurus_adv(*args, key_sort='none'):
    """
    @param args: N number of strings in format Name and Lastname, ['name lastname', ...]
    @type args: str
    @param key_sort: allow to sort list
                    - 'none' is default, list will be returned as is
                    - 'asc', list will be returned in ascending order
                    - 'desc', list will be returned in descending order
    @type key_sort: str
    @return: dictionary of Name and Lastnames
    @rtype: dict
    """
    main_list = {}
    original_values = []

    for name in args:
        original_values.append(name)

        name_cap = ' '.join(elem.capitalize() for elem in name.split())
        sub_list = {}
        name_sep = name_cap.split(' ')
        first_name = name_sep[0]
        last_name = name_sep[1]
        # добавил капитализацию первых букв, потому что захотел
        key_first_name = first_name[0][0].capitalize()
        key_last_name = last_name[0][0].capitalize()

        if main_list.get(key_last_name) is not None:
            if main_list.get(key_last_name).get(key_first_name) is not None:
                main_list.get(key_last_name).get(key_first_name).append(name_cap)
        else:
            sub_list[key_first_name] = [name_cap]
            main_list[key_last_name] = sub_list

    print(f'Список изначальных значений: {original_values}')
    if key_sort == 'asc':
        main_list_sorted = {}
        for k, v in sorted(main_list.items()):
            for k2, v2 in sorted(v.items()):
                v[k2] = sorted(v2)
            main_list_sorted[k] = v
        print(main_list_sorted)
    elif key_sort == 'desc':
        main_list_sorted = {}
        for k, v in sorted(main_list.items(), reverse=True):
            for k2, v2 in sorted(v.items()):
                v[k2] = sorted(v2, reverse=True)
            main_list_sorted[k] = v
        print(main_list_sorted)
    else:
        # в этой задаче я не стал делать проверку на key_sort
        # и решил пусть все в одни ворота, если не одно из нужных значения
        print(main_list)


print(f'Вывод без сортировки:')
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

print(f'\nВывод с сортировкой по возрастанию:')
thesaurus_adv("инна серова", "иван сергеев", "питер альбертович", "петр алексеев", "илья иванов", "анна савельева",
              key_sort='asc')

print(f'\nВывод с сортировкой по убыванию:')
thesaurus_adv("инна серова", "иван сергеев", "питер альбертович", "петр алексеев", "илья иванов", "анна савельева",
              key_sort='desc')
