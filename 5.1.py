# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open("HomeWork5.1", "w") as HomeWork:
    text = input("Введите текст: ")
    while text:
        HomeWork.write(text+'\n')
        text = input("Введите следующий текст или нажмите 'Enter' для завершения: ")