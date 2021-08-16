# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров.
# Проверьте корректность полученного результата.
class Complex:
    # def __init__(self, r, m , *args):
    def __init__(self, r, m):
        self.r = r
        self.m = m

    def __add__(self, other):
        return Complex(self.r + other.r, self.m + other.m)

    def __mul__(self, other):
        return Complex(self.r * other.r - self.m * other.m, self.r * other.m + self.m * other.r)

    def __str__(self):
        return f"{self.r} + i{self.m}"


my_complex1 = Complex(10, 8)
my_complex2 = Complex(3, 9)
print(f"Сумма чисел: {my_complex1 + my_complex2}")
print(f"Произведение чисел: {my_complex1 * my_complex2}")
