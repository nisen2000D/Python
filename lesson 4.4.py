my_list = [2, 33, 12, 12, 2, 4, 9, 77, 34, 10, 11, 10]
non_repeating = [el for el in my_list if my_list.count(el) < 2]
print(non_repeating)
