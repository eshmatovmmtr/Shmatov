
a_list = ['Зима', 'Весна', 'Лето', 'Осень']
b_dict = {1: 'Зима', 2: 'Весна', 3: 'Лето', 4: 'Осень'}
winter = 1, 2, 12
spring = 3, 4, 5
summer = 6, 7, 8
autumn = 9, 10, 11
month = int(input("Введите номер месяца(от 1 до 12): "))
if month in winter:
    print(a_list[0] + " " + b_dict.get(1))
elif month in spring:
    print(a_list[1] + " " + b_dict.get(2))
elif month in summer:
    print(a_list[2] + " " + b_dict.get(3))
elif month in autumn:
    print(a_list[3] + " " + b_dict.get(4))
else:
    print("Такого номера месяца не существует!")