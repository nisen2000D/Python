my_dict = {}
with open('my_file_6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject, lecture, practice, lab = line.split()
        my_dict[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов: \n {my_dict}')
