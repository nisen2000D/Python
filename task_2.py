import random

array = [round(random.uniform(1, 50)) for i in range(10)]
print(f'Исходный массив: {array}')


def merge_sort(a):
    if len(a) < 2:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:len(a)])

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1

    while i < len(left):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while j < len(right):
        a[k] = right[j]
        j = j + 1
        k = k + 1
    return a


print(f'Отсортированный массив: {merge_sort(array)}')