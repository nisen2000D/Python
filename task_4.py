user = int(input('Вводите по одному числу (enter - закончить): '))
a = []
while True:
    try:
        a.append(user)
        user = int(input('-- '))
    except:
        break
print(a)

b = set(a)
most_num = None
quantity = 0

for i in b:
    q = a.count(i)
    if q > quantity:
        quantity = q
        most_num = i

print(most_num)