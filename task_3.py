import random
m = 4
size = 2 * m + 1
lst3 = [random.randint(1, 50) for i in range(size)]

print(f'Исходный список: {lst3}')


def median(lst):
    if len(lst) % 2 == 0:
        center = []

        for i in lst:
            b = sum(i < j for j in lst)

            if len(lst) in [b * 2 + 2, b * 2]:
                center.append(i)
        return sum(center) / 2

    else:
        for i in lst:
            num = i
            b = sum(num < j for j in lst)

            if len(lst) == 2 * b + 1:
                return num


print(f'Медиана: {median(lst3)}')

print(f'Отсортированный список: {sorted(lst3)}')