class ComplexNumber:
    def __init__(self, num_1, num_2, *args):
        self.num_1 = num_1
        self.num_2 = num_2

    def __add__(self, other):
        print(f'Сложение:')
        return f'{self.num_1 + other.num_1} + {self.num_2 + other.num_2} = {self.num_1 + other.num_1 + self.num_2 + other.num_2}'

    def __mul__(self, other):
        print(f'Умножение:')
        return f'{self.num_1 * other.num_1} + {self.num_2 * other.num_2} = {self.num_1 * other.num_1 + self.num_2 * other.num_2}'

    def __str__(self):
        return f'{self.num_1} + {self.num_2} = {self.num_1 + self.num_2}'


num_1 = ComplexNumber(1, 2)
num_2 = ComplexNumber(3, 4)
print(num_1)
print(num_2)
print(num_1 + num_2)
print(num_1 * num_2)
