with open('my_file_3.txt', 'r', encoding='utf-8') as f:
    workers = {}
    middle = []
    m = []
    for line in f:
        key, value = line.split()
        workers[key] = value
        middle.append(value)
        if int(value) < 20000:
            print(f'{key}: зарплата меньше 20000')
print(f'Средний оклад {sum(map(int, middle)) / len(middle)}')
