"""
Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield,например:
- odd_to_15 = odd_nums(15)
- next(odd_to_15)
1
- next(odd_to_15)
3
...
- next(odd_to_15)
15
- next(odd_to_15)
...StopIteration...

*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно)
не используя ключевое слово yield.
"""


def odd_nums(seq):
    arr = [i for i in range(seq+1) if i % 2 != 0]
    return iter(arr)


sequence = int(input('До какого числа включительно генерируем нечетные числа?: '))
odd_to_15 = odd_nums(sequence)
while odd_to_15:
    try:
        print(next(odd_to_15))
    except StopIteration:
        print('Генератор опустошен')
        break
