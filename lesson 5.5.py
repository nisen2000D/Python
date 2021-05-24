with open('my_file_5.txt', 'w+') as f:
    line = input('Введите цифры через пробел: ')
    f.writelines(line)
    num = line.split()

    print(sum(map(int, num)))
