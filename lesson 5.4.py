rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('my_file_4.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        new_file.append(rus[i[0]] + '  ' + i[1])
    print(new_file)

with open('my_file_4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_file)
