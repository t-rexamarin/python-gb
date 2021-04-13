# -*- coding: utf-8 -*-
"""
*(вместо 1) Написать регулярное выражение для парсинга файла логов web-сервера из ДЗ 6 урока nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
для получения информации вида:
(<remote_addr>, <request_datetime>, <request_type>, <requested_resource>, <response_code>, <response_size>),
например:
raw = '188.138.60.101 - - [17/May/2015:08:05:49 +0000] "GET /downloads/product_2 HTTP/1.1" 304 0 "-"
            "Debian APT-HTTP/1.3 (0.9.7.9)"'
parsed_raw = ('188.138.60.101', '17/May/2015:08:05:49 +0000', 'GET', '/downloads/product_2', '304', '0')

Примечание: вы ограничились одной строкой или проверили на всех записях лога в файле?
Были ли особенные строки?
Можно ли для них уточнить регулярное выражение?
"""
# регулярка не совсем оптимальна, кое где ее можно было бы улучшить
# сделал просто принт


import re

# просто наброски того, с чего работал, решил не удалять
# "^(?P<req_ip>(\d{,3}\.){3}\d{,3}) - - (?P<req_date>\[\d{,2}.+\])" lazy
# ^(?P<req_ip>(\d{,3}\.){3}\d{,3}).+(?P<req_date>\[\d{,2}.+\]) "(?P<req_type>\w{,6})
# (?P<req_resourse>[/\w]+).+(?P<res_code>\d{3}) (?P<req_size>\d+)

# ^(?P<req_ip>(\d{,3}\.){3}\d{,3}).+\[(?P<req_date>\d{2}[/]\w{3}[/]\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]
# "(?P<req_type>\w{,6}) (?P<req_resourse>[/\w]+).+(?P<res_code>\d{3}) (?P<req_size>\d+)

# ^(?P<req_ip>(\d{,3}\.){3}\d{,3}).+\[(?P<req_date>\d{2}[/]\w{3}[/]\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]
# "(?P<req_type>\w+) (?P<req_resourse>[/\w]+).+(?P<res_code>\d{3}) (?P<req_size>\d+)

# ^(?P<req_ip>(\d{1,3}\.){3}(\d{1,3})|(\w{0,4}:){1,7}(\w{0,4})).+\
# [(?P<req_date>\d{2}[/]\w{3}[/]\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]
# "(?P<req_type>\w+) (?P<req_resourse>[/\w]+).+(?P<res_code>\d{3}) (?P<req_size>\d+)


def parse_line(line_to_parse):
    reg_ex = re.compile(r'^(?P<req_ip>(\d{1,3}\.){3}(\d{1,3})|(\w{0,4}:){1,7}(\w{0,4})).+'
                        r'\[(?P<req_date>\d{2}[/]\w{3}[/]\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\] '  # не нравится ему \[
                        r'"(?P<req_type>\w+) '
                        r'(?P<req_resourse>[/\w]+).+'
                        r'(?P<res_code>\d{3}) '
                        r'(?P<req_size>\d+)')

    results = reg_ex.search(line_to_parse)
    remote_addr = results.group('req_ip')
    request_datetime = results.group('req_date')
    request_type = results.group('req_type')
    requested_resource = results.group('req_resourse')
    response_code = results.group('res_code')
    response_size = results.group('req_size')

    result_str = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)

    return result_str


with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    with open('nginx_result.txt', 'w', encoding='utf-8') as f_w:
        line = f.readline()
        # print(parse_line(line))

        while line:
            # print(parse_line(line))
            f_w.write(line)
            line = f.readline()
