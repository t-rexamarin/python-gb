class Cell:
    def __init__(self, inner_cells: int):
        self.inner_cells = int(inner_cells)

    def __add__(self, other: int):
        """
        Сложение. Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        @param other:
        @type other:
        @return:
        @rtype:
        """
        # ворнинг на то что а other(int) нет аттрибута inner_cells, даже хз, стоит такое как то лечить
        cells_sum = self.inner_cells + other.inner_cells

        return Cell(cells_sum)

    def __sub__(self, other):
        """
        Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества
        ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
        @param other:
        @type other:
        @return:
        @rtype:
        """
        if self.inner_cells - other.inner_cells > 0:
            rounded_result = self.inner_cells - other.inner_cells

            return rounded_result
        else:
            msg = f'Разница кол-ва ячеек двух клеток меньше или равно 0'
            raise Exception(msg)

    def __mul__(self, other):
        """
        Умножение. Создаётся общая клетка из двух.
        Число ячеек общей клетки — произведение количества ячеек этих двух клеток.
        @param other:
        @type other:
        @return:
        @rtype:
        """
        rounded_result = Cell(self.inner_cells * other.inner_cells)

        return rounded_result

    # из-за указания возвращаемых типов будут ворнинги
    # указывал от части для себя
    def __floordiv__(self, other):
        """
        Целочисленное деление
        @param other:
        @type other:
        @return:
        @rtype: int
        """
        rounded_result = Cell(self.inner_cells // other.inner_cells)

        return rounded_result

    def __truediv__(self, other):
        """
        Дробное деление
        @param other:
        @type other:
        @return:
        @rtype: float
        """
        rounded_result = Cell(self.inner_cells / other.inner_cells)

        return rounded_result

    def make_order(self, inner_cells_in_line: [int]) -> str:
        """
        Метод возвращает строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу
        @param inner_cells_in_line:
        @type inner_cells_in_line:
        @return:
        @rtype: str
        """
        result = ''
        arr = []
        tmp_line = ''
        elem_counter = self.inner_cells

        # есть кол-во ячеек клетки 10
        # есть кол-во ячеек в линии 3
        # 3 3 3 1

        # подумать над условиями
        for elem in range(self.inner_cells + 1):
            if len(tmp_line) < inner_cells_in_line and elem_counter > 0:
                tmp_line += '*'
            elif len(tmp_line) == inner_cells_in_line:
                arr.append(tmp_line)
                tmp_line = '*'
            elif elem_counter == 0:
                arr.append(tmp_line)

            elem_counter -= 1

        result += '\n'.join(arr)

        return result


cell_1 = Cell(10)
cell_2 = Cell(8)
cell_after_truediv_division = cell_1.__truediv__(cell_2)
cell_after_floordiv_division = cell_1.__floordiv__(cell_2)


# print(cell_1.__add__(cell_2))
print('Длинна ячейки 10, вывод по 3 в ряд')
print(cell_1.make_order(3))
print('\n')
print('Длинна ячейки 10, вывод по 12 в ряд')
print(cell_1.make_order(12))
print('\n')
print(cell_after_truediv_division.make_order(2))
print('\n')
print(cell_after_floordiv_division.make_order(2))
