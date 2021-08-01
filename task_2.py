from collections import deque


def sum_hex(x, y):
    m_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    transfer = 0

    x, y = (deque(y), deque(x)) if len(y) > len(x) else (deque(x), deque(y))
    while x:

        if y:
            res = m_num[x.pop()] + m_num[y.pop()] + transfer

        else:
            res = m_num[x.pop()] + transfer

        transfer = 0

        if res < 16:
            result.appendleft(m_num[res])

        else:
            result.appendleft(m_num[res - 16])
            transfer = 1

    if transfer:
        result.appendleft('1')

    return list(result)


def mult_hex(x, y):
    m_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    spam = deque([deque() for _ in range(len(y))])

    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = m_num[y.pop()]

        for j in range(len(x) - 1, -1, -1):
            spam[i].appendleft(m * m_num[x[j]])

        for _ in range(i):
            spam[i].append(0)

    transfer = 0

    for _ in range(len(spam[-1])):
        res = transfer + sum(spam[i].pop() for i in range(len(spam)) if spam[i])

        if res < 16:
            result.appendleft(m_num[res])

        else:
            result.appendleft(m_num[res % 16])
            transfer = res // 16

    if transfer:
            result.appendleft(m_num[transfer])

    return list(result)


a = list(input('Введите 1 число: ').upper())
b = list(input('Введите 2 число: ').upper())
# print(a, b)

print(*a, '+', *b, '=', *sum_hex(a, b))

print(*a, '*', *b, '=', *mult_hex(a, b))