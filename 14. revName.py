name = input("Enter you name: ")
revName = ""

for i in range(len(name)-1, 0-1, -1):
    revName += name[i]

print("Reversed of enter name is: ",revName)