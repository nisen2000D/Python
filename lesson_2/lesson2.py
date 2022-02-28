"""1. Задание на закрепление знаний по модулю CSV.
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt, info_3.txt
и формирующий новый «отчетный» файл в формате CSV. Для этого:
Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными,
их открытие и считывание данных.
В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
 значения параметров
 «Изготовитель системы»,
 «Название ОС»,
 «Код продукта»,
 «Тип системы».
Значения каждого параметра поместить в соответствующий список.
Должно получиться четыре списка — например,
os_prod_list,
os_name_list,
os_code_list,
os_type_list.
В этой же функции создать главный список для хранения данных отчета — например,
main_data — и поместить в него названия столбцов отчета в виде списка:
    «Изготовитель системы»,
    «Название ОС»,
    «Код продукта»,
    «Тип системы».
Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;
Проверить работу программы через вызов функции write_to_csv().
"""
import re, csv, chardet, json, yaml


def get_data():
    files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
            content = content.decode(chardet.detect(content)['encoding'])
            os_prod_list = file, re.findall('Изготовитель системы:\s+(\w+)', content)[0].strip()
            os_name_list = file, re.findall('Название ОС:\s+([\w\.\s]+)\n', content)[0].strip()
            os_code_list = file, re.findall('Код продукта:\s+([\w\-]+\w+)', content)[0].strip()
            os_type_list = file, re.findall('Тип системы:\s+([\w\-\w\s\w]+)', content)[0].strip()

            main_data.extend([[os_prod_list[1], os_name_list[1], os_code_list[1], os_type_list[1]]])

    return main_data


def write_to_csv(csv_file):
    to_write = get_data()
    with open(csv_file, 'w', encoding='utf-8', newline="") as main_data_file:
        md_writer = csv.writer(main_data_file, quoting=csv.QUOTE_ALL, quotechar="\"")
        md_writer.writerow(to_write[0])
        md_writer.writerows(to_write[1:], )
    return print(f'Данные записаны в файл: {csv_file}')


"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
 Написать скрипт, автоматизирующий его заполнение данными. Для этого:
Создать функцию write_order_to_json(), в которую передается 5 параметров:
товар (item),
количество (quantity),
цена (price),
покупатель (buyer),
дата (date).
Функция должна предусматривать запись данных в виде словаря в файл orders.json. 
При записи данных указать величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра. 
"""


def write_order_to_json(item, quantity, price, buyer, date):
    order_dict = \
        {'orders': {
            'Товар': item,
            'Количество': quantity,
            'Цена': price,
            'Покупатель': buyer,
            'Дата': date}}

    with open('orders.json', 'w', encoding='utf-8') as o:
        json.dump(order_dict, o, indent=4, ensure_ascii=False)

    return print('Данные записаны в файл: orders.json')


"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, 
автоматизирующий сохранение данных в файле YAML-формата. Для этого:
Подготовить данные для записи в виде словаря,
в котором первому ключу соответствует список, 
второму — целое число, 
третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
отсутствующим в кодировке ASCII (например, €);
Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью параметра default_flow_style,
а также установить возможность работы с юникодом: allow_unicode = True;
Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными."""


def write_to_yaml():
    data_for_yaml = {'first_key': ['list', 'of', 'keys'],
                     'second_key': 67,
                     'third_key': {'inner_key1': '33Ѱ', 'inner_key8': '21※', 'inner_key3': '17€'}
                     }

    with open('file.yaml', 'w', encoding='utf-8') as file_yaml:
        yaml.dump(data_for_yaml, file_yaml, default_flow_style=False, allow_unicode=True)
        print('Данные записаны в файл: file.yaml')

    with open('file.yaml', 'r', encoding='utf-8') as file_yaml:
        print('Загрузка данных из: file.yaml')
        date_from_yaml_file = yaml.load(file_yaml, Loader=yaml.SafeLoader)
        if date_from_yaml_file == data_for_yaml:
            print('Данные совпадают!')


if __name__ == '__main__':
    write_to_csv('main.csv')
    write_order_to_json(item='Пончик', quantity='7', price='35', buyer='Павел', date='01.05.2021')
    write_to_yaml()
