from random import random

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num = int(random() * (num2 - num1 + 1)) + num1
print(num)

n1 = float(input('Введите первое число: '))
n2 = float(input('Введите первое число: '))
n = random() * (n2 - n1) + n1
print(round(n, 3))

s1 = ord(input('Введите случайный символ: '))
s2 = ord(input('Введите случайный символ: '))
n = int(random() * (s2 - s1 + 1)) + s1
print(chr(n))