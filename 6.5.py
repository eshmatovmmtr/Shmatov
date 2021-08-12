# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса
# Pen (ручка),
# Pencil (карандаш),
# Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    name = "Канцелярская принадлежность"

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    name = "Ручка"

    def draw(self):
        print(f"Вы рисуете {self.name}(ой)")


class Pencil(Stationery):
    name = "Карандаш"

    def draw(self):
        print(f"Вы рисуете {self.name}ом")


class Handle(Stationery):
    name = "Маркер"

    def draw(self):
        print(f"Вы рисуете {self.name}ом")


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
