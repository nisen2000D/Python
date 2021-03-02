class Equipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена: {self.price} количество: {self.quantity}'

    def information(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за единицу: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства:': unit, 'Цена за единицу:': unit_p, 'Количество:': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Список: \n {self.my_store}')
        except:
            return 'Ошибка ввода'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(' ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад: \n {self.my_store_full}')
            return 'Выход'
        else:
            return Equipment.information(self)


class Printer(Equipment):
    def print(self):
        return ' '


class Scanner(Equipment):
    def scan(self):
        return ' '


class Copier(Equipment):
    def copier(self):
        return ' '


printer = Printer('Epson', 2000, 123, 2)
scanner = Scanner('Sumsung', 3000, 12, 16)
copier = Copier('Xerox', 4000, 5, 10)
print(printer.information())
print(scanner.information())
print(copier.information())
print(printer.print())
print(copier.copier())
