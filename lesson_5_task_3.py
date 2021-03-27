"""
Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...

Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
"""
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]

klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

klasses_short = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def my_gen(pupils, classes):
    for k, v in enumerate(pupils):
        try:
            school_tutor = pupils[k]
        except IndexError:
            school_tutor = None

        try:
            school_class = classes[k]
        except IndexError:
            school_class = None

        # row = (school_tutor, school_class)
        yield school_tutor, school_class


# норм
# my_genn = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
# print(my_gen)

# my_gen = my_gen(tutors, klasses_short)
print('У каждого элемента tutors есть пара из klasses')
my_gen_long = my_gen(tutors, klasses)
for i in tutors:
    print(next(my_gen_long))

print('\n')
print('У каждого элемента tutors есть пара из klasses')
my_gen_short = my_gen(tutors, klasses_short)
for x in tutors:
    print(next(my_gen_short))
