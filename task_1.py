user_str = str(input("Введите строку: "))

print(f'Длина строки "{user_str}": {len(user_str)} символов')

subs_set = set()
for i in range(len(user_str)):
    for j in range(len(user_str) - 1 if i == 0 else len(user_str), i, -1):
        subs_set.add(hash(user_str[i:j]))
print(f'Количество подстрок: {len(subs_set)}')