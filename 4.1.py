# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
# def my_func():
#     try:
#         time = float(input('Количество отработанных часов: '))
#         salary = int(input('Ставка за час: '))
#         bonus = int(input('Премия: '))
#         res = time * salary + bonus
#         print(f'Заработная плата сотрудника составляет: {res}')
#     except ValueError:
#         return print('Не является числом')
#
#
# my_func()

from sys import argv

script_name, first_param, second_param, third_param = argv

try:
    time = float(first_param)
    salary = int(second_param)
    bonus = int(third_param)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
