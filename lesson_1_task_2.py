"""
2.
Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
    Внимание: использовать только арифметические операции!
К каждому элементу списка добавить 17
    и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
    Внимание: новый список не создавать!!!
"""
# выводы закоменчены, т.к. про вывод информации в задаче нет ни слова :)

my_list = []

for i in range(1000):
    if i % 2 != 0:
        my_list.append(i ** 3)

numbers_sum_divided_by_7 = 0
for number in my_list:
    digits_sum = 0
    for digit in str(number):
        digits_sum += int(digit)
    if digits_sum % 7 == 0:
        numbers_sum_divided_by_7 += number

# print('Сумма кубов чисел от 0 до 1000, сумма цифр которых делится нацело на 7:', numbers_sum_divided_by_7)

for i in range(0, len(my_list)):
    my_list[i] += 17

numbers17_sum_divided_by_7 = 0
for number in my_list:
    digits_sum = 0
    for digit in str(number):
        digits_sum += int(digit)
    if digits_sum % 7 == 0:
        numbers17_sum_divided_by_7 += number

# print('Сумма чисел, к которым было прибавлено 17, сумма цифр которых делится нацело на 7:', numbers17_sum_divided_by_7)
