from random import random

a = []
for i in range(4):
    b = []
    for s in range(5):
        n = int(random() * 100)
        b.append(n)
        print('%4d' % n, end='')
    a.append(b)
    print()

max_a = -1
for s in range(5):
    min_a = 100
    for i in range(4):
        if a[i][s] < min_a:
            min_a = a[i][s]
    if min_a > max_a:
        max_a = min_a
print("Максимальное среди минимальных чисел: ", max_a)