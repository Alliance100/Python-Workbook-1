# Create a Student class with name, age, marks, and a method that returns pass/fail.

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


name = input("Enter student name: ")
age = int(input("Enter student age: "))
marks = float(input("Enter student marks: "))

student = Student(name, age, marks)

print(f"{student.name}: {student.pass_fail()}")