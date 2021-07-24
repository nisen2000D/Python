from random import random
maxTryCount = round(random() * 100)
i = 1
while i <= 10:
    u = int(input(f'Угадайте число от 0 до 100: '))
    if u > maxTryCount:
        print('Слишком большое число')
    elif u < maxTryCount:
        print('Слишком маленькое число')
    else:
        print('Поздравляю! Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('10 попыток закончились. Было загадано', maxTryCount)