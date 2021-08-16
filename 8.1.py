# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        self.date = date

    @classmethod
    def extract(cls, date):
        try:
            day, month, year = date.split(".")
            return int(day), int(month), int(year)
        except Exception as e:
            print(f"Ошибка! {e}")

    @staticmethod
    # if 1 <= day <= 31:
    #     if 1 <= month <= 12:
    #         if 2019 >= year >= 0:
    #             return f'All right'
    #         else:
    #             return f'Неправильный год'
    #     else:
    #         return f'Неправильный месяц'
    # else:
    #     return f'Неправильный день'
    def data(date_input):
        try:
            day, month, year = date_input
            if day not in range(1, 32):
                raise ValueError('Некорректно указан день!')
            elif month not in range(1, 13):
                raise ValueError('Некорректно указан месяц!')
            elif year not in range(2000, 2101):
                raise ValueError('Неккоректно указан год!')
        except ValueError as e:
            print(e)
        else:
            print('Правильная дата')


my_date_cls = Date('16.08.2021')
my_date = my_date_cls.extract(my_date_cls.date)
print(my_date)
if my_date:
    my_date_cls.data(my_date)
