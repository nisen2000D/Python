my_list = []
for i in range(4):
    l = []
    s = 0
    print(f"{i+1} строка:")
    for _ in range(5 - 1):
        n = int(input())
        s += n
        l.append(n)
    l.append(s)
    my_list.append(l)

for i in my_list:
    print(i)