# Add a __str__ method so that print(student) gives readable output.

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def pass_fail(self):
        if self.marks >= 50:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Marks: {self.marks}"


name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = float(input("Enter student marks: "))

student = Student(name, age, marks)

print(student)