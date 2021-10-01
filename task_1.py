num = int(input('Введите трёхзначное число: '))
num1 = num % 10
num2 = num % 100 // 10
num3 = num // 100

print("Сумма:", num1 + num2 + num3)
print("Произведение:", num1 * num2 * num3)
