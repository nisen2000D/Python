f = open('my_file_1.txt', 'w', encoding='utf-8')
user_text = None
while user_text != "":
    user_text = input('Введите текст: ')
    f.write(f'{user_text}\n')
f.close()
