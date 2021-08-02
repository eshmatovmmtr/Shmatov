# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.
def my_func():
    sum_res = 0
    ex = False
    while not ex:
        n = input('Введите числа через пробел, если захотите выйти введите "E" - ').split()
        res = 0
        for el in range(len(n)):
            if n[el] == 'e' or n[el] == 'E':
                ex = True
                break
            else:
                res = res + int(n[el])
        sum_res = sum_res + res
        print(f'Сумма чисел: {sum_res}')
    print(f'Окончательная сумма чисел: {sum_res}')


my_func()