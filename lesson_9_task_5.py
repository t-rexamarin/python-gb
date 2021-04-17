"""
Реализовать класс Stationery (канцелярская принадлежность):
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        pass


class Pen(Stationery):
    def draw(self):
        msg = f'It is the {self.title} method, and should be the Pen method.'
        return msg


class Pencil(Stationery):
    def draw(self):
        msg = f'It is the {self.title} method, and should be the Pencil method.'
        return msg


class Handle(Stationery):
    def draw(self):
        msg = f'It is the {self.title} method, and should be the Handle method.'
        return msg


pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

st_arr = {'Pen': pen,
          'Pencil': pencil,
          'Handle': handle}

for key, stationary in st_arr.items():
    print(stationary.draw())
