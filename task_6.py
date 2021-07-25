from random import random
a = []
for i in range(10):
    a.append(int(random() * 50))
print(a)
print()
min_index = 0
max_index = 0
for i in range(1,10):
    if a[i] < a[min_index]:
        min_index = i
    elif a[i] > a[max_index]:
        max_index = i
print(f'Min: {a[min_index]}  Max: {a[max_index]}')
if min_index > max_index:
    min_index, max_index = max_index, min_index
summa = 0
for i in range(min_index+1, max_index):
    summa += a[i]
print(f'Sum: {summa}')