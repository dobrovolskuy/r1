class Student:

    total_students = 0
    def __init__(self,name):
        self.name = name

        Student.total_students +=1

    @classmethod
    def display_total_students(cls):
        print(f"Total number of students {cls.total_students}")

student1 = Student(name = "Oleg")
student2 = Student(name= "Petro")
Student.display_total_students()

