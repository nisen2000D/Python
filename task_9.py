a, b, c = map(int, input('Введите три числа: ').split())

if b < a < c or c < a < b:
    print('Среднее число:', a)
elif a < b < c or c < b < a:
    print('Среднее число:', b)
else:
    print('Среднее число:', c)