# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы:
# go,
# stop,
# turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов:
# TownCar,
# SportCar,
# WorkCar,
# PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name}, цвета {self.color} выдвинулась со скоростью {self.speed} км/ч")

    def stop(self):
        print(f"Машина {self.name}, цвета {self.color} остановилась")

    def turn(self, direction):
        print(f"Машина {self.name}, цвета {self.color} повернула на {direction}")

    def show_speed(self):
        print(f"Текущая скорость машины {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


town_car = TownCar(70, "Черный(ого)", "BMW", False)
town_car.go()
town_car.turn("право")
town_car.show_speed()
town_car.stop()

sport_car = SportCar(120, "Хаки", "Ferrari")
sport_car.go()
sport_car.show_speed()
sport_car.stop()
sport_car.turn("лево")
sport_car.go()

work_car = WorkCar(40, "красный(ого)", "Reno", False)
work_car.go()
work_car.turn("лево")
work_car.go()
work_car.turn("право")
work_car.show_speed()
work_car.stop()

police_car = PoliceCar(100, "Белосиний(его)", "Ford")
police_car.go()
police_car.show_speed()
police_car.turn("право")
police_car.stop()
