from itertools import count
from math import factorial


def fact(n):
    for el in count(n):
        yield factorial(el)


x = 0
for el in fact(1):
    if x < 15:
        print(el)
        x += 1
    else:
        break
