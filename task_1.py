while True:
    try:
        num_1, num_2 = map(int, input('Введите 2 числа: ').split())
        sign = input('Введите знак: ')
    except ValueError:
        print('Неправильный ввод')
        continue

        # Проверка
    if sign == '0':
        print('Завершение')
        break
    elif sign == '+':
        print(f'{num_1} {sign} {num_2} = {num_1 + num_2}')
    elif sign == '-':
        print(f'{num_1} {sign} {num_2} = {num_1 - num_2}')
    elif sign == '*':
        print(f'{num_1} {sign} {num_2} = {num_1 * num_2}')
    elif sign == '/':
        try:
            print(f'{num_1} {sign} {num_2} = {num_1 / num_2}')
        except ZeroDivisionError:
            print('Ошибка. Деление на ноль')



