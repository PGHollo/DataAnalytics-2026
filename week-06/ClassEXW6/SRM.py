class Student:
   
    School = "YearUp Academy"

    def __init__(self, name, __grade, track):
        self.name =name
        self.grade = __grade
        self.track = track
    
    def get_grade(self):
        return self.grade
    
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.grade = new_grade
        else:
            print("Invalid grade. Enter a value between 0 and 100.")

    def display_info(self):
        print(f"Student School: {self.School}")
        print(f"Grade: {self.get_grade()}")
        print(f"Track: {self.track}")

student1 = Student("Frank", 95, "Data Analyst") 
student2 = Student("Joe", 70, "Software Developer") 
student1.display_info()
student2.display_info()

