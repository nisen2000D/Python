a = int(input('Введите число: '))
even = 0
odd = 0
while a > 0:
    if a % 2 == 0:
        even += 1
    else:
        odd += 1
    a //= 10
print("Чётных: %d" % (even))
print("Нечётных: %d" % (odd))