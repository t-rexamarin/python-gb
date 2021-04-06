"""
*(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
"""

import requests
import operator

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get(url)
r_content = r.text

# print(type(r_content))
with open('logs.txt', 'w+', encoding='utf-8') as f:
    f.writelines(r_content)

    f.seek(0)
    line = f.readline()
    result = {}
    tmp = []
    while line:
        str_to_arr = line.split(' ')
        request_ip = str_to_arr[0]
        # request_type = str_to_arr[5][1:]
        # request_url = str_to_arr[6]

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
            print(f'Почетное {i} место {sorted_result[i]}')
    # print(max(sorted_result))
    # max_result = max(result.values())
    # print(max_result)
