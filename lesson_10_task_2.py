"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани.
Проверить на практике полученные на этом уроке знания.
Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
"""
from abc import ABC, abstractmethod
import random


class Clothes(ABC):
    _material_total = 0

    @abstractmethod
    def material_calc(self):
        pass

    """
    1. это вообще нехорошо в проперть прятать что-то, что изменяет данные
          проперть может вычислять и возвращать значение вычисленное или закешированное
    2. к атрибуту класса внутри методов надо обращаться через пространство имён класса или объекта
          т.е. через self (или cls для класс-методов), или прямо через имя класса
    """
    # переделал
    @classmethod
    def get_total_material(cls):
        material_total_rounded = round(cls._material_total, 2)

        return material_total_rounded


class Coat(Clothes):
    # требование "которая может иметь определённое название" понял так
    # если явно не задано, будет None
    def __init__(self, v: int, name=None):
        if isinstance(v, (int, float)):
            self.name = name
            self.v = v
        else:
            msg = f'V must be int. You have passed V({type(v)}).'
            raise Exception(msg)

    @property
    def material_calc(self):
        """
        Подсчет материала на пальто
        @return: строка с названием модели и кол-во необходимого материала
        @rtype: float
        """
        try:
            material_needed = round((self.v / 6.5 + 0.5), 2)
            Clothes._material_total += material_needed

            return material_needed
        except Exception as e:
            msg = f'Что то пошло не так {e}'
            return msg


class Suit(Clothes):
    def __init__(self, h: int, name=None):
        if isinstance(h, (int, float)):
            self.name = name
            self.h = h
        else:
            msg = f'H must be int. You have passed H({type(h)}).'
            raise Exception(msg)

    @property
    def material_calc(self):
        """
        Подсчет материала на костюм
        @return: строка с названием модели и кол-во необходимого материала
        @rtype: float
        """
        try:
            material_needed = round((2 * self.h + 0.3), 2)
            Clothes._material_total += material_needed

            return material_needed
        except Exception as e:
            msg = f'Что то пошло не так {e}'
            return msg


all_clothes = {}

for i in range(4):
    random_size = random.randint(30, 60)
    all_clothes[f'пальто{i}'] = Coat(random_size)

for i in range(4):
    random_size = random.randint(30, 60)
    all_clothes[f'костюм{i}'] = Suit(random_size)

material_total = 0
for k, value in all_clothes.items():
    material_total += value.material_calc
material_total = round(material_total, 2)

"""
удвоение значения в Clothes.material_total происходит из-за того
что в коде для всех созданных объектов одежды подсчёт материала запускается дважды
"""
# понял, вот это место
# for key, item in all_clothes.items():
#     print(item.material_calc)

print(f'Для изготовления {len(all_clothes)} вещей, потребуется {material_total} единиц ткани.')
print(f'Значение material_total из основного класса Clothes {Clothes.get_total_material()}.')
