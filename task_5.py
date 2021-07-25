from random import random
my_list = [int(random() * 100) - 50 for _ in range(10)]
print(my_list)

index = -1
for i in range(10):
    if index == -1:
        if my_list[i] < 0:
            index = i
    elif my_list[i] > my_list[index]:
        if my_list[i] < 0:
            index = i
print(f'Число: {my_list[index]}')
print(f'Индекс: {index}')