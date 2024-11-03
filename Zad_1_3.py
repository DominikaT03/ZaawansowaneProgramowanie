class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return sum(self.marks) / len(self.marks) > 50

student1 = Student("Anna", [50, 60, 80])
student2 = Student("Damian", [20, 40, 50])

print(student1.name, "passed:", student1.is_passed())
print(student2.name, "passed:", student2.is_passed())