# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Узнаем число
n = int(input("Введите число: "))
nn = (n*11)
nnn = (n*111)
# Узнаем сумму
summary = (n + nn + nnn)
# Выводим сумму
print(str(summary))