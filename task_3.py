num = int(input('Введите число: '))
m = 0
while num > 0:
    m = m * 10 + num % 10
    num //= 10
print(m)