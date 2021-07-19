# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
# Вводим значения выручки и издержек
a = int(input("Введите значение выручки: "))
b = int(input("Введите значение издержек: "))
# Если выручка больше издержек
if int(a > b):
    # Высчитываем рентабельность выручки
    r = (((a - b) / a) * 100)
    # Вводим количество сотрудников
    k = int(input("Введите количество сотрудников: "))
    # Высчитываем прибыль в расчете на одного сотрудника
    s = (r / k)
    print(f"Рентабельность выручки составляет: {r} Прибыль фирмы в расчете на одного сотрудника составляет: {s}")
    # Если выручка меньше издержек
elif int(a < b):
    # Высчитываем убытки
    y = (a - b)
    print(f"Издержки больше выдержки, вы понесли убытки в сумме: {y}")