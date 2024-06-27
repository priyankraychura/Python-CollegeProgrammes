list = [10, 25, 15, 22, 87, 99, 22, 25, 10]
newList = []

for item in list:
    if item not in newList:
        newList = newList + [item]

print(newList)