user_list = [int(s) for s in input('Введите числа через пробел: ').split()]
min_index = 0
max_index = 0
for i in range(1, len(user_list)):
    if user_list[i] > user_list[max_index]:
        max_index = i
    if user_list[i] < user_list[min_index]:
        min_index = i
user_list[min_index], user_list[max_index] = user_list[max_index], user_list[min_index]
print(' '.join([str(i) for i in user_list]))