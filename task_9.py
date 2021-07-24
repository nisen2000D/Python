n = int(input('Введите числа (Нажмите "q", чтобы вывести наибольшее число и сумму): '))
max_s = 0
max_n = 0
while n != 'q':
    m = int(n)
    s = 0
    while int(n) > 0:
        s += int(n) % 10
        n = int(n) // 10
    if s > max_s:
        max_s = s
        max_n = m
    n = input()

print(f'Число {max_n}, максимальная сумма цифр: {max_s}')