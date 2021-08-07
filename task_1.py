# Версия Python: python 3.9.1 x32
# Windows 10 x64

import sys

def show_size(x, level=0):
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par


# ЗАДАНИЕ: Сформировать из введенного числа обратное по порядку входящих в него цифр
# и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

new_num = ''

num = input('Введите число: ')
count = len(num)
k = range(count)

for _ in k:
    new_num += str(int(num) % 10)
    num = int(num) // 10
print(new_num)

sum_member2 = show_size(new_num) + show_size(num) + show_size(count) + show_size(k)
print('Выделено памяти: {}'.format(sum_member2))
