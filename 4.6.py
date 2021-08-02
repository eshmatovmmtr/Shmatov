# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного
from itertools import count


def my_func(a, b):
    for el in count(a):
        if el > b:
            break
        else:
            print(el)


my_func(int(input("Введине начальное число: ")), int(input("Введите конечное число: ")))
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
from itertools import cycle

my_list = ["Hello", "it`s", "me"]
a = int(input("Введите количество повторений: "))
i = 1
f = cycle(my_list)
while i <= a:
    i = i + 1
    print(next(f))
