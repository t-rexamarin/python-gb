"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]
"""

import requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get(url)
r_content = r.text

with open('logs.txt', 'w+') as f:
    f.writelines(r_content)

    f.seek(0)
    line = f.readline()
    while line:
        str_to_arr = line.split(' ')
        request_ip = str_to_arr[0]
        request_type = str_to_arr[5][1:]
        request_url = str_to_arr[6]

        my_tuple = (request_ip, request_type, request_url)
        print(my_tuple)
        line = f.readline()
