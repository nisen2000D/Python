import random

lst = [random.randint(-100, 100) for i in range(10)]
print(f'Список : {lst}')

def sort_list(lst):
    n = 1

    while n < len(lst):
        sorted = True

        for i in range(len(lst) - n):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted = False

        if sorted == True:
            break

        n += 1

    print(f'Отсортированный список: {lst}')


sort_list(lst)