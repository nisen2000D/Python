from collections import namedtuple

QUARTERS = 4
Company = namedtuple('Company', ['name', 'quarters', 'profit'])
all_companies = set()

num = int(input("Введите количество предприятий: "))
total_profit = 0
for i in range(1, num + 1):
    profit = 0
    quarters = []
    name = input(f'Введите название {i} предприятия : ')

    for j in range(QUARTERS):
        quarters.append(int(input(f'Прибыль за {j + 1}-ый квартал: ')))
        profit += quarters[j]

    comp = Company(name=name, quarters=tuple(quarters), profit=profit)

    all_companies.add(comp)
    total_profit += profit

average = total_profit / num
print('-'*100)
print(f'Средняя прибыль всех предприятий: {average}')

print('-'*100)
print(f'Предприятия с прибылью выше среднего:')
for comp in all_companies:
    if comp.profit > average:
        print(f'Компания "{comp.name}" заработала: {comp.profit}')

print('-'*100)
print(f'Предприятия с прибылью ниже среднего:')
for comp in all_companies:
    if comp.profit < average:
        print(f'Компания "{comp.name}" заработала: {comp.profit}')