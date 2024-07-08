numbers = open("numbers.txt")
even = open("even.txt", "a")
odd = open("odd.txt", "a")

for num in numbers:
    if int(num)%2 == 0:
        even.write(num)
    else:
        odd.write(num)

even.close()
odd.close()