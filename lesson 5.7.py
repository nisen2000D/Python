import json
profit = {}
pr = {}
prof = 0
middle = 0
i = 0
with open('my_file_7.txt', 'r') as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        middle = prof / i
        print(f'Средняя прибыль: {middle:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')
    pr = {'Средняя прибыль': round(middle)}
    profit.update(pr)
    print(f'Прибыль каждой компании: {profit}')

with open('my_file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'json файл: \n '
          f' {js_str}')