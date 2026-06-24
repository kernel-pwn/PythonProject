# shared among all instances of a class
# defined outside the constructor
# allow you to share the data among all objects created from that class

class student:

    class_year =2024
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        student.num_student += 1

student1 = student("Pedro", 18)
student2 = student("Maria", 22)
student3 = student("spongebob", 32)

# print(student1.num_student)

print(f"my graduating class of {student.class_year} has {student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)