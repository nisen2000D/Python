from random import random
a = []
for i in range(10):
    a.append(int(random() * 100))
print(a)
print()

if a[0] > a[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

print(f'Наименьшие числа: {a[min1]} и {a[min2]}')
