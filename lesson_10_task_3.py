class Cell:
    def __init__(self, inner_cells):
        self.inner_cells = int(inner_cells)

    def __add__(self, other: [int]):
        """
        Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        @param other:
        @type other:
        @return:
        @rtype:
        """
        # возвращать новый экземпляр?
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
            rounded_result = int(self.inner_cells - other.inner_cells)

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
        rounded_result = Cell(int(self.inner_cells * other.inner_cells))

        return rounded_result

    def __floordiv__(self, other):
        rounded_result = Cell(int(self.inner_cells // other.inner_cells))

        return rounded_result

    def __truediv__(self, other):
        rounded_result = Cell(int(self.inner_cells / other.inner_cells))

        return rounded_result

    def make_order(self, inner_cells_in_line: [int]) -> str:
        result = ''
        # result = None
        arr = []
        tmp_line = ''
        elem_counter = self.inner_cells

        # есть кол-во ячеек клетки 10
        # есть кол-во ячеек в линии 3
        # 3 3 3 1

        # подумать над условиями
        for elem in range(self.inner_cells+1):
            if len(tmp_line) < inner_cells_in_line and elem_counter > 0:
                # print('1')
                tmp_line += '*'
            elif len(tmp_line) == inner_cells_in_line:
                # print('2')
                arr.append(tmp_line)
                tmp_line = '*'
            elif elem_counter == 0:
                # print('0')
                arr.append(tmp_line)

            elem_counter -= 1

        result += '\n'.join(arr)

        return result


cell_1 = Cell(10)
cell_2 = Cell(8)

# print(cell_1.__add__(cell_2))
print(cell_1.make_order(3))
