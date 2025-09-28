students = [("Johnny", "C"),("Mason", "A"),("Anna", "B"),("Emma", "A"),("DreamyBull", "C"),("Noah", "F"),("James", "C")]

print("Class list:")
student = lambda student: student[0]
students.sort(key=student)
for s in students:
    print(s)

print("Rank students by their grades:")
grade = lambda grade: grade[1]
students.sort(key=grade)
for s in students:
    print(s)