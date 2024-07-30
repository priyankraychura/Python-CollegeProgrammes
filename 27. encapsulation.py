class Student:
    def __init__(self, name, age):
        self.name = name        
        self.__age = age        

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.__age}")

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age. Age must be positive.")

student = Student("John Doe", 21)
print(student.name)  

try:
    print(student.__age)
except AttributeError as e:
    print(e)  

print(student.get_age())  
student.set_age(22)
print(student.get_age())  
