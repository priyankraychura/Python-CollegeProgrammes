def insertion_sort(inputList):
    for i in range(1, len(inputList)):
        j = i - 1
        nxt_element = inputList[i]

        while(inputList[j] > nxt_element) and (j >= 0):
            inputList[j+1] = inputList[j]
            j =  j - 1
            inputList[j+1] = nxt_element

list = [12, 56, 11, 25, 3, 69, 77, 22]
insertion_sort(list)
print(list)