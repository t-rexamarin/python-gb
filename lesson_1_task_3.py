"""
3.
Реализовать склонение слова «процент» для чисел до 20.
Например, задаем число 5 — получаем «5 процентов», задаем число 2 — получаем «2 процента».
Вывести все склонения для проверки.
"""
# буду придираться к постановке :)
# сказано "для чисел до 20", но не сказано от какого числа
# так или иначе, работет с любым диапазоном целых чисел
# про дроби не сказано, работа с ними исключена
# "Например, задаем число" - дает мне основание полагать, что должен быть функционал ввода,
# помимо вывода всех склонения для проверки, поэтому дополнительно реализовано с использованием input

while True:
    try:
        percent = int(input('Введите целое число: '))
        break
    except ValueError:
        print('Вы указали не целое число')

grp_1 = ('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')
grp_2 = '1'
grp_3 = ('2', '3', '4')

percent_text = 'процент'
grp_1_ending = 'ов'
grp_3_ending = 'а'

percent_as_str = str(percent)
if percent_as_str.endswith(grp_1):
    percent_final_text = percent_text + grp_1_ending
    print(percent_as_str, percent_final_text)
elif percent_as_str.endswith(grp_2):
    print(percent_as_str, percent_text)
elif percent_as_str.endswith(grp_3):
    percent_final_text = percent_text + grp_3_ending
    print(percent_as_str, percent_final_text)

print('Вывод всех склонений от 0 до 20:')
for i in range(21):
    str_i = str(i)
    if str_i.endswith(grp_1):
        percent_final_text = percent_text + grp_1_ending
        print(str_i, percent_final_text)
    elif str_i.endswith(grp_2):
        print(str_i, percent_text)
    elif str_i.endswith(grp_3):
        percent_final_text = percent_text + grp_3_ending
        print(str_i, percent_final_text)
