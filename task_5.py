a = ord(input('Введите первую букву: '))
b = ord(input('Введите вторую букву: '))
a = a - ord('a') + 1
b = b - ord('a') + 1
print('На каких местах: %d и %d' % (a, b))
print('Сколько между ними находится букв:', abs(a - b) - 1)
