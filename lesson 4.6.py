# а) итератор, генерирующий целые числа, начиная с указанного:
from itertools import count

for el in count(int(input('Введите число: '))):
    if el <= 100:
        print(el)
    else:
        break
# б) итератор, повторяющий элементы некоторого списка, определенного заранее:
from itertools import cycle

my_list = [True, 'ABC', 123, None]
i = 0
for el in cycle(my_list):
    if i < 10:
        print(el)
        i += 1
    else:
        break
