def facto(num):
    if num == 1:
        return 1
    else:
        return(num * facto(num-1))
    
n = int(input("Enter a number: "))
print("The factorial of the number is: ", facto(n))

# def facto(num, fact):
#     if num == 1 or num == 0:
#         return fact
    
#     fact = fact * num
#     num -= 1

#     return facto(num, fact)
    
    
# num = int(input("Enter the number: "))
# fact = 1
# ans = facto(num, fact)
# print("Factorial of the number is: ", ans)

