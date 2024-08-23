students = {}
courses = {}

while True:
    command = input()
    if command == 'end':
        break

    register = command.split(" : ")
    course = register[0]
    student = register[1]

    if student not in students.keys():
        students[student] = course
    if course not in courses.keys():
        courses[course] = 0
    courses[course] += 1

for course, quantity in courses.items():
    print(f'{course}: {quantity}')
    students_in_course = {student: lect for (student, lect) in students.items() if lect == course}
    for student, course in students_in_course.items():
        print(f'-- {student}')

