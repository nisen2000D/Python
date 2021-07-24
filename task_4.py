num = int(input('Введите количество элементов: '))
a = 1
b = 0
for i in range(num):
    b += a
    y = i + 1
    print(f' {y}) {a}')
    a /= -2

print('Сумма: ', b)