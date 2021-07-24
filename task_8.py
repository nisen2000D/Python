num = int(input("Введите количество чисел: "))
a = int(input("Какую цифру нужно посчитать: "))
count = 0
for i in range(1, num + 1):
    m = int(input(f" {str(i)}) "))
    while m > 0:
        if m % 10 == a:
            count += 1
        m = m // 10

print(f'{count} раз(а) была введена цифра {a}')