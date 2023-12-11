class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades
    def __len__(self):
        return len(self.grades)

student1 = Student(name="Oleg", surname="Dobrovolskuy", grades=[10, 11, 9, 12,10])
student2 = Student(name="Igor", surname="Kylpa", grades=[7, 5, 9, 10])
student3 = Student(name="Maryan", surname="Lapka", grades=[4, 8, 7])

students = [student1, student2, student3]

sorted_students = sorted(students, key=lambda x: len(x.grades), reverse=True)

for student in sorted_students:
    print(f"{student.name} {student.surname} - count: {len(student)}")
