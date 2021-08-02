# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
a = int(input("Введите первое значение: "))
b = int(input("Введите второе значение: "))
c = int(input("Введите третье значение: "))


def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a >= b and c >= b:
        return a + c
    else:
        return b + c


print(f'Результат - {my_func(a, b, c)}')
