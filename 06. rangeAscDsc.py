start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

order = input("Enter asc or des as order: ")

if order == "asc":
    for num in range(start, end+1):
        print(num)
elif order == "des":
    temp = start
    start = end
    end = temp
    for num in range(start, end-1, -1):
        print(num)
else:
    print("Invalid choice")


