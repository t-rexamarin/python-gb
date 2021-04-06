import requests

url = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
r = requests.get(url)
r_content = r.text

# print(type(r_content))
with open('logs.txt', 'a+') as f:
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
    # str_to_arr = f.readline().split(' ')
    # print(str_to_arr)
