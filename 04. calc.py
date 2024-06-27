num1 = eval(input("Enter value 1: "))
num2 = eval(input("Enter value 2: "))

print("\nEnter 1 for Addition.")
print("Enter 2 for Substration.")
print("Enter 3 for Multiplication.")
print("Enter 4 for DIvison")

input = int(input("\nEnter the chouce: "))

if input == 1:
    print("\nAddition is: ", num1 + num2)
elif input == 2:
    print("\nSubstration is: ", num1 - num2)
elif input == 3:
    print("\nMultiplication is: ", num1 * num2)
elif input == 4:
    print("\nDivison is: ", num1 / num2)
else:
    print("\nInvalid Choice")

