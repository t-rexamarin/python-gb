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
# это первый, более ленивый вариант


class Matrix:
    def __init__(self, matrix: [list]):
        self.matrix = matrix

    def __str__(self):
        str_result = ''

        # подумать над более компактной записью
        for i in range(len(self.matrix)):
            if i == len(self.matrix) - 1:
                str_result += ' '.join(str(char) for char in self.matrix[i])
            else:
                str_result += ' '.join(str(char) for char in self.matrix[i]) + '\n'

        return str_result

    def __add__(self, other):
        result_list = []

        # TODO: проверка на одинаковую длинну
        for key, line in enumerate(self.matrix):
            matrix_line = []
            for key2, char in enumerate(line):
                matrix_line.append(self.matrix[key][key2] + other[key][key2])
            result_list.append(matrix_line)
        return Matrix(result_list)


my_matrix = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
# print(my_matrix)
my_matrix_2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(my_matrix.__add__(my_matrix_2))
