"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
num_translate("one")
    "один"
num_translate("eight")
    "восемь"

Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода:
    какой тип данных выбрать, в теле функции или снаружи.

*(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной.
Например:
num_translate_adv("One")
    "Один"
num_translate_adv("two")
    "два"
"""

translations = {'zero': 'ноль',
                'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}


def num_translate_adv(item_to_translate):
    if item_to_translate.lower() in translations:
        if item_to_translate[0].isupper():
            print(translations[f'{item_to_translate.lower()}'].capitalize())
        else:
            print(translations[f'{item_to_translate.lower()}'])
    else:
        print('None')
        # return None


numbers = input('Введите значение(я) (zero, one, Two, thREE, four, five, sIX, Seven, Eight, Nine, ten, eleven): ')
numbers = list(numbers.replace(' ', '').split(','))

for number in numbers:
    num_translate_adv(number)
