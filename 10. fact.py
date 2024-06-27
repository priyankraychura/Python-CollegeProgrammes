def facto(num, fact):
    if num == 1 or num == 0:
        return fact
    
    fact = fact * num
    num -= 1

    return facto(num, fact)
    
    
num = int(input("Enter the number: "))
fact = 1
ans = facto(num, fact)
print("Factorial of the number is: ", ans)

