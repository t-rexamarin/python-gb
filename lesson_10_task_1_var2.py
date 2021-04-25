"""
Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
    который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31  22      3   5   32      3   5   8   3
37  43      2   4   6       8   3   7   1
51  86      -1  64  -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для  сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно.
Первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""
# это второй вариант, он выше кмк по-лучше


class Matrix:
    def __init__(self, my_list: [list]):
        self.my_list = my_list

    def __str__(self):
        str_result = ''

        # подумать над более компактной записью
        for i in range(len(self.my_list)):
            if i == len(self.my_list) - 1:
                str_result += ' '.join(str(char) for char in self.my_list[i])
            else:
                str_result += ' '.join(str(char) for char in self.my_list[i]) + '\n'

        return str_result

    def __add__(self, other):
        if len(self.my_list) == len(other):
            for elem1, elem2 in zip(self.my_list, other):
                if len(elem1) == len(elem2):
                    matrix_line = [list(map(lambda x: x[0] + x[1], zip(elem1, elem2)))
                                   for elem1, elem2 in zip(self.my_list, other)]
                else:
                    msg = f'Строки матриц должны быть одной длинны. Ошибка между {elem1} и {elem2}'
                    raise Exception(msg)

                return Matrix(matrix_line)
        else:
            # думаю со временем пойму, что лучше рейзить
            msg = f'Матрицы должны быть одного размера'
            raise Exception(msg)
            # raise AssertionError(msg)


my_matrix = Matrix([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
my_matrix_2 = [[4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7]]

# в последней строке больше символов, чем у основной матрицы
# my_matrix_2 = [[4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7, 8]]

# больше на 1 элемент, чем основная матрица
# my_matrix_2 = [[4, 5, 6, 7], [4, 5, 6, 7], [4, 5, 6, 7], [8, 9, 0]]
print(my_matrix.__add__(my_matrix_2))
