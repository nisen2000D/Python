user = int(input('Вводите по одному числу (enter - закончить): '))
first_list = []
while True:
    try:
        first_list.append(user)
        user = int(input('-- '))
    except:
        break

second_list = [i for i in range(len(first_list)) if first_list[i] % 2 == 0]
print(first_list)
print('Индексы чётных чисел: ', second_list)