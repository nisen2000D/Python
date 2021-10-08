from random import random
my_list = []
for i in range(10):
    my_list.append(int(random() * 100) - 50)
print(my_list)

i = 0
index = -1
while i < 10:
    if my_list[i] < 0 and index == -1:
        index = i
    elif my_list[i] < 0 and my_list[i] > my_list[index]:
        index = i
    i += 1

print(f'Число: {my_list[index]}')
print(f'Индекс: {index}')