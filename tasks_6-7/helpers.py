# объявляю переменную, чтобы ссылаться всегда на один источник
bakery_file = 'bakery.csv'


def is_digit(arg):
    try:
        float(arg)
        return True
    except ValueError:
        return False


def indexes_check(start_index, stop_index):
    # массив для текста ошибки, т.к. результат ф-ции выводится распаковкой с сепаратором
    txt_msg = []
    start_index_mod = None
    stop_index_mod = None

    if start_index is None:
        return start_index, stop_index
    elif start_index is not None:
        try:
            start_index = int(start_index)
        except ValueError:
            txt_msg.append(f'Стартовый индекс({start_index}) не является числом')
            return txt_msg
        else:
            if start_index <= 0:
                txt_msg.append(f'Стартовый индекс({start_index}) не может быть меньше 1')
                return txt_msg
            else:
                # т.к. мы работает со срезом
                start_index_mod = start_index - 1

        if stop_index is not None:
            try:
                stop_index = int(stop_index)
            except ValueError:
                txt_msg.append(f'Конечный индекс({stop_index}) не является числом')
                return txt_msg
            else:
                if stop_index < start_index:
                    txt_msg.append(f'Конечный индекс({stop_index}) не может быть меньше стартового({start_index})')
                    return txt_msg
                elif stop_index == start_index:
                    # чтобы не хватать лишнее, то без изменения
                    stop_index_mod = stop_index
                elif stop_index > start_index:
                    stop_index_mod = stop_index

    return start_index_mod, stop_index_mod


# TODO: if __name__ == '__main__' ?
# по идее он не нужен, т.к. тут нет вызовов функций
# а переменная мне как раз нужна
