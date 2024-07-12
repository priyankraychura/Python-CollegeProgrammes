def fileReadUpper(fileName):
    try:
        file = open(fileName)
    except FileNotFoundError:
        print("File not found")
    else:
        for ch in file:
            print(ch.upper())
        
fileReadUpper("demo1.txt")