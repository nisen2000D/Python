n = int(input('Введие число: '))
s = 0
for i in range(1, n+1):
    s += i
m = round(n * (n + 1) / 2)
print(f'{s}={m}')
