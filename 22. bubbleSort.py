def bubble_sort(list):
    for itr_num in range(len(list) - 1, 0, -1):
        for idx in range(itr_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp

list = [12, 58, 5, 47, 11, 26, 3, 8, 99]
bubble_sort(list)
print(list)