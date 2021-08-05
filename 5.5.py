# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open("HomeWork5.5", "w") as HomeWork:
    s = input("Введите числа через пробел: ")
    HomeWork.writelines(s)
    l = s.strip().split()
    n = [float(ns) for ns in l if ns.isdigit()]
    print(sum(n))
