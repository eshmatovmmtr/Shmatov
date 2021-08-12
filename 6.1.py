# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность
# первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
from itertools import cycle
from time import sleep


class TrafficLight:
    colors = ("красный", "желтый", "зеленый")
    times = (7, 2, 10)
    text = ("Стоп!", "Приготовиться!", "Марш!")

    def __init__(self, color):
        self.__color = color

    def running(self):
        mc = cycle(self.colors)
        for time_color in mc:
            if self.__color == time_color:
                print(self.text[self.colors.index(self.__color)])
                sleep(self.times[self.colors.index(self.__color)])
                self.__color = next(mc)


traffic = TrafficLight("красный")
traffic.running()
