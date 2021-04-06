"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
"""
# ох, не знаю, что то я тут сделал
# сделал чуть другой вывод, нежели просила задача, осознанно
# дописвал и перепроверял уже в спешке, время поджимало
# у меня только сомнения на счет считывания, но вроде бы читается строго построчно и память не должна забиться
# но с другой стороны, перечитать весь файл в массив даст как раз эффект выхода за память...
# не было много время подумать над этим

import requests
import operator

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

with requests.get(url, stream=True) as r:
    with open('logs.txt', 'w+', encoding='utf-8') as f:
        # chunk_size=None. A value of None will function differently depending on the value of stream
        # сам определит размер?
        for chunk in r.iter_content(chunk_size=512, decode_unicode=True):
            # print(sys.getsizeof(next(chunk)))
            # print(type(next(chunk)))
            f.write(chunk)

        f.seek(0)
        line = f.readline()
        result = {}
        tmp = []
        while line:
            str_to_arr = line.split(' ')
            request_ip = str_to_arr[0]

            if request_ip not in tmp:
                result[request_ip] = 1
                tmp.append(request_ip)
            else:
                result[request_ip] += 1

            line = f.readline()

        sorted_result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
        for i in range(10):
            if i == 0:
                print(f'Абсолютный спаммер чемпион {sorted_result[i]}')
            else:
                print(f'Почетное {i+1} место {sorted_result[i]}')
