print_list = []
a = int(input("Введите желаемое количество элементов: "))
for i in range(a):
    c = int(input("Введите элемент: "))
    print_list.append(c)
n = 0
for elem in range(int(len(print_list)/2)):
    print_list[n], print_list[n + 1] = print_list[n + 1], print_list[n]
    n += 2
print(print_list)
