from functools import reduce


def my_func(i, el):
    return i * el


print(f'Чётные числа: {[el for el in range(100, 1001,2)]}')
print(f'Результат вычисления: {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')
