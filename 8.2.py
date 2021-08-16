# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.
class AnException(Exception):
    def __init__(self):
        self.txt = 'Производится деление на ноль'


# @staticmethod
#     def segmentation(delimoe, delitel):
#         try:
#             return (delimoe / delitel)
#         except:
#             return (f"Производится деление на ноль")
def segmentation(delimoe, delitel):
    try:
        if delitel == 0:
            raise AnException
        print(delimoe / delitel)
    except AnException as error:
        print(error.txt)


segmentation(15, 0)
# div = AnException(10, 100)
# print(AnException.segmentation(10, 0))
# print(AnException.segmentation(10, 0.1))
# print(div.segmentation(100, 0))
