f = open('my_file_2.txt', 'r')
content = f.read()
print(f'Содержимое файла: \n {content}')
f = open('my_file_2.txt', 'r')
content = f.readlines()
print(f'Количество строк: {len(content)}')
f = open('my_file_2.txt', 'r')
content = f.readlines()
for i in range(len(content)):
    print(f'В {i + 1} строке: {len(content[i])} символов')
f = open('my_file_2.txt', 'r')
content = f.read()
print(f'Количество слов: {len(content.split())}')
f.close()
