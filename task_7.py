a = int(input("1 сторона: "))
b = int(input("2 сторона: "))
c = int(input("3 сторона: "))

if a + b <= c or a + c <= b or b + c <= a:
    print("Ошибка. Вы ввели неверные данные")
elif a != b and a != c and b != c:
    print("Треугольник - разносторонний")
elif a == b == c:
    print("Треугольник - равносторонний")
else:
    print("Треугольник - равнобедренный")