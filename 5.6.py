# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

# s = {}
# with open('HomeWork5.6', 'r') as init_f:
#     for line in init_f:
#         subject, *pr = line.split()
#         s[subject] = [int(f.rstrip('(л)(пр)(лаб)')) for f in pr if f != '—']
#         s.update({subject: sum(s)})
#     print(s)


s = {}
with open("HomeWork5.6", "r") as HomeWork:
    for line in HomeWork:
        disc, *par = line.split()
        lc = [int(l.strip('(л)(пр)(лаб)')) for l in par if l != '—']
        s.update({disc: sum(lc)})

print(s)

