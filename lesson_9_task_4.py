"""
Реализуйте базовый класс Car:
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы:
    go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
"""
# немного не доделал момент определения is_police в дочерних классах - доделаю


class Car:
    def __init__(self, speed, color, name, is_police):
        if isinstance(is_police, bool):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police
        else:
            msg = f'is_police must be bool. You got {type(is_police)}.'
            print(msg)

    def go(self):
        msg = 'The car is moving.'
        return msg

    def stop(self):
        msg = 'The car has stopped.'
        return msg

    def turn(self, direction):
        # не стал выпендриваться и добавлять всяких проверок
        msg = f'The car has turned {direction}.'
        return msg

    def show_speed(self):
        msg = f'The car speed is {self.speed}.'
        return msg


class TownCar(Car):
    def show_speed(self):
        speed_limit = 60

        if self.speed > speed_limit:
            msg = f'Speed limit is {speed_limit}. Your speed is {self.speed}!'
            return msg
        else:
            msg = f'Your speed is fine.'
            return msg


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        speed_limit = 40

        if self.speed > speed_limit:
            msg = f'Speed limit is {speed_limit}. Your speed is {self.speed}!'
            return msg
        else:
            msg = f'Your speed is fine.'
            return msg


# не было времени подумать над этим, пока оставлю так
# как бы логично, что у этого класса is_police должно быть True, у других false
# чуть позже доделаю
# class PoliceCar(Car):
#     def __init__(self, speed, color, name, is_police):
#         super().__init__(speed, color, name, is_police)
#         self.is_police = True
class PoliceCar(Car):
    pass


def print_separator():
    print('*' * 30 + '\n')


town_car = TownCar(71, 'blue', 'bmw', False)
town_car_2 = TownCar(59, 'red', 'bmw', False)
sport_car = SportCar(100, 'red', 'porshe', False)
work_car = WorkCar(41, 'yellow', 'subaru', False)
work_car_2 = WorkCar(30, 'blue', 'subaru', False)
police_car = PoliceCar(66, 'white', 'secret car', True)
# police_car2 = PoliceCar(66, 'white', 'secret car')

cars_arr = {'Town_car': town_car,
            'Town_car_2': town_car_2,
            'Sport_car': sport_car,
            'Work_car': work_car,
            'Work_car_2': work_car_2,
            'Police_car': police_car}

for key, car in cars_arr.items():
    print(f'{key}. Speed: {car.speed}, '
          f'color: {car.color}, '
          f'name: {car.name}, '
          f'is police: {car.is_police}')
    print(car.go())
    print(car.stop())
    print(car.turn('right'))
    print(car.show_speed())
    print_separator()
