student_grades = {}
loop_range = int(input())

for index in range(loop_range):
    student = input()
    grade = float(input())

    if student not in student_grades.keys():
        student_grades[student] = {}
        student_grades[student]['grades'] = []
    student_grades[student]['grades'].append(grade)

for student, value in student_grades.items():
    for grade, result in value.items():
        average = sum(result) / len(result)
        if average >= 4.50:
            print(f"{student} -> {average:.2f}")

