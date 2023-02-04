
"""define the getter and setter methods for the name and marks attributes in class"""
class Student:
    def setName(self, name):
        self.name = name

    def setMarks(self, marks):
        self.marks = marks

    def getName(self):
        return self.name

    def getMarks(self):
        return self.marks

n = int(input("Enter the number of students: "))
students = []

for i in range(n):
    name = input("Enter the student's name: ")
    marks = input("Enter the student's marks: ")

    s = Student()
    print(s.__dict__)
    s.setName(name)
    s.setMarks(marks)
    students.append(s) # students list consists of refrences of the objects
    print(s.__dict__) # it will print all the data members associated with the object s
print(students)
for i in students:
    print("Hello, ", i.getName())
    print("Marks are", i.getMarks(), "\n")

