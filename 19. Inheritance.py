class Parent:
    def __init__(self, fname, fage):
        self.firstname = fname
        self.age = fage

    def view(self):
        print("This is Parent class view: ")
        print(self.firstname, self.age)

class Child(Parent):
    def __init__(self, fname, fage, clg):
        Parent.__init__(self, fname, fage)
        self.college = clg

    def view(self):
        print("This is Child class view: ")
        print(f"My name is {self.firstname}. I am {self.age} years old. I study in {self.college}.")

p1 = Parent("Priyank", 21)
p1.view()
ob = Child("ABC", 22, "Christ College")
ob.view()

