list = ["Priyank", "Ra", "G", "Da", "Hiren"]

print("Max value string: ", max(list, key=len))

print("String with more than 2 char: ")
for item in list:
    if len(item) > 2:
        print(item)

