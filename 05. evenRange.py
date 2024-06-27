start = int(input("Enter the start: "))
end = int(input("Enter the end: "))

print("Even number is range: ")
while(start <= end):
    if start % 2 != 0:
        print(start)

    start = start + 1

# for num in range(start, end+1):
#     if num % 2 == 0:
#         print(num)