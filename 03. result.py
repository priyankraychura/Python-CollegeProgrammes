name = input("Enter name: ")
sem = input("Enter semester: ")
college = input("Enter college name: ")

j2ee = eval(input("Enter J2EE marks: "))
python = eval(input("Enter Python marks: "))
cyberS = eval(input("Enter Cyber Security marks: "))

total = j2ee + python + cyberS
perc = (total/300) * 100

if perc >= 90 and perc <=100:
    clasS = "Distinction!"
elif perc >=80 and perc <= 89:
    clasS = "First Class"
elif perc >=60 and perc <= 79:
    clasS = "Second Class"
elif perc >=40 and perc <=59:
    clasS = "Third Class"
else:
    clasS = "Failed!"

print("\n\nName: ", name)
print("Semester: ", sem)
print("College: ", college)
print("Total Marks: ", total)
print("Percentage: ", perc)
print("Class", clasS)




