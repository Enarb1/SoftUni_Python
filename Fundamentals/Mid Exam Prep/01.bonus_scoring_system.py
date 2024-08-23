from math import ceil

students_num = int(input())
lectures_num = int(input())
additional_bonus = int(input())

attendance = []

for _ in range(students_num):
    student = int(input())
    attendance.append(student)

max_student = max(attendance)
print(f"Max Bonus: {ceil(max_student / lectures_num * (5 + additional_bonus))}.")
print(f"The student has attended {max_student} lectures.")
