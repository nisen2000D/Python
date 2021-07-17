x1, y1, x2, y2 = [int(x) for x in input('Введите кординаты (x1 y1 x2 y2): ').split()]
print("Уравнение:")
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(" y = %.2f*x + %.2f" % (k, b))