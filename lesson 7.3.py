class Cell:
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return f'Сумма: {self.param + other.param}'

    def __sub__(self, other):
        ans = self.param - other.param
        if ans >= 0:
            return f'Разность: {ans}'
        else:
            return 'Число отрицательное'

    def __mul__(self, other):
        return f'Умножение: {self.param * other.param}'

    def __truediv__(self, other):
        return f'Деление: {int(self.param / other.param)}'

    def make_order(self, num):
        result = ''
        for i in range(int(self.param / num)):
            result += '*' * num + '\n'
        result += '*' * (self.param % num) + '\n'
        return result


cell_1 = Cell(40)
cell_2 = Cell(7)
print(cell_1.__add__(cell_2))
print(cell_1.__sub__(cell_2))
print(cell_1.__mul__(cell_2))
print(cell_1.__truediv__(cell_2))
print(cell_1.make_order(10))
