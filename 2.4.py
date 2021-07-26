String = input("Введите слово/несколько слов через пробел: ")
s_string = []
n = 0
for word in range(String.count(' ') + 1):
    s_string = String.split()
    n += 1
    if len(str(s_string)) <= 10:
        print(f"{n}: {s_string[word]}")
    else:
        print(f"{n}: {s_string[word] [0:10]}")