a = [0, 0, 0, 0, 0, 0, 0, 0]
for i in range(2, 100):
    for b in range(2, 10):
        if i % b == 0:
            a[b-2] += 1
i = 0
while i < 8:
    print(f'Кратность числу {i+2} - {a[i]}')
    i += 1