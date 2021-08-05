# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
with open("HomeWork5.1", "r") as HomeWork:
    line = HomeWork.readline()
    print(f"Количество строк в файле: {len(line)}")
    for word, value in enumerate(line):
        print(f"Количество слов в строке {format(word + 1)}: {len(value.split())}")
