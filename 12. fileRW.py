file = open("demo.txt", "w")
file.write("Hello world!")
file.close()

file = open("demo.txt")
print(file.read())