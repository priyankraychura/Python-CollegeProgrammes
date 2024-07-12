def reverseName(name):
    revName = ""

    for i in range(len(name)-1, 0-1, -1):
        revName += name[i]

    return revName

name = input("Enter you name: ")
print("Reversed of enter name is: ",reverseName(name))