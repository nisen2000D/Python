num = [34, 12, 7, 7, 9, 23, 9, 6, 2, 2, 8, 10, 11]
num_list = [number for i, number in enumerate(num) if i > 0 and num[i] > num[i - 1]]
print(num_list)
