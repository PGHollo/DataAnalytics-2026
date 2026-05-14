class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Grade: {self.grade}")
        print("---------------------")



student1 = Student("Alice", 95)
student2 = Student("Brian", 88)


print(f"Student 1: {student1.name} {student1.grade}")
print(f"Student 2: {student2.name} {student2.grade}")


student1.display_info()
student2.display_info()