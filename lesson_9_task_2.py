"""
Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу:
    длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
    толщиной в 1 см*число см толщины полотна;
проверить работу метода.

Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""
# честно, формулировка меня немного сбила, надеюсь я все правильно написал
# возможно, итоговая формула вышла немного топорно, моя техническая база страдает)
# изначально просто делил на 1000 итог, чтобы привести к тоннам, но мне не очень нравилось
# немного пришлось подсмотреть
# а друг технарь сказал, что формулу вообще бы надо по другому сделать, используя плотность


class Road:
    def __init__(self, length: [int, float], width: [int, float]):
        """
        @param length: длинна пдорожного полотна в метрах
        @type length: [int, float]
        @param width: ширина пдорожного полотна в метрах
        @type width: [int, float]
        """
        if isinstance(length, (int, float)) and isinstance(width, (int, float)):
            self._length = length
            self._width = width
            # по умолчанию слой 1 см, но вдруг изменится
            self._layer_thickness = 1
        else:
            # если в ините идут проверки, возврат делать через принт?
            # или надо оборачивать все в функцию и делать ретурн?
            msg = f'Length and width must be int or float. You passed length({type(length)}), width({type(width)}).'
            print(msg)

    # вроде правильно написал
    # но при ошибках turn возвращает строки, которые при такой нотации будут ворнинги давать
    # тогда такое использовать некорректно? или как раз все верно?
    def mass_calc(self, thickness: [int, float]) -> [float]:
        """
        @param thickness: толщина слоя в сантиметрах
        @type thickness: [int, float]
        @return: масса асфальта в тоннах
        @rtype: float
        """
        # на 1 кв метр 25 кг асфальта
        # это я уже для себя пишу:) 1кв.м. 10000 см
        mass = 25

        if isinstance(thickness, (int, float)):
            try:
                # м * м * кг * см
                result = (self._length * self._width * mass * ((self._layer_thickness * thickness) / 100)) * 0.1
                return result
            except AttributeError as e:
                msg = f'Error occurred: {e}.'
                return msg
            except Exception as e:
                msg = f'An unexpected error occurred: {e}.'
                return msg
        else:
            msg = f'Thickness must be int or float. You passed thickness({type(thickness)}).'
            return msg


calc = Road(20.0, 5000)
# calc = Road('str', 5000)
print(f'Необходимая масса сфальта в тоннах: {calc.mass_calc(5)}')
