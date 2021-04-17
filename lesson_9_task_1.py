"""
Создать класс TrafficLight (светофор):
    определить у него один атрибут color (цвет) и метод running (запуск);
    атрибут реализовать как приватный;
    в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
    продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
        третьего (зелёный) — на ваше усмотрение;
    переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
    проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов.
При его нарушении выводить соответствующее сообщение и завершать скрипт.

"""
import time
from termcolor import colored


class TrafficLight:
    # color_seq = None

    def __init__(self, __color):
        self.__color = __color

    def running(self):
        mode = self.__color
        color_seq = {'red': 7, 'yellow': 2, 'green': 10}

        # проверка на наличие такого цвета
        if mode in color_seq.keys():
            color_start_from = list(color_seq).index(mode)
            colors = list(color_seq)[color_start_from:]

            for color in colors:
                txt_colored = colored(f'{color}', color)
                print(f'{txt_colored} for {color_seq[color]} sec')
                time.sleep(color_seq[color])
        else:
            print('no such mode')


# my_class = TrafficLight('blue') # не существует
my_class = TrafficLight('red')
# my_class = TrafficLight('yellow')
# my_class = TrafficLight('green')
my_class.running()
