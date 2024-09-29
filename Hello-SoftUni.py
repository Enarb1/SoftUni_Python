def result_print(courses_and_students, courses,invalid_students):
    result = ""

    for course_num, student_names in courses_and_students:
        for name in student_names:
            result += (f"*** A student with the username {name} has successfully "
                       f"finished the course {courses[course_num]}!\n")

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"

    return result


def softuni_students(*students, **courses):
    courses_and_students = {}
    invalid_students = []

    for course_id, student in students:
        if course_id in courses.keys():
            if course_id not in courses_and_students.keys():
                courses_and_students[course_id] = []
            courses_and_students[course_id].append(student)
            courses_and_students[course_id] = sorted(courses_and_students[course_id])
        else:
            invalid_students.append(student)

    sorted_courses_and_students = sorted(courses_and_students.items(), key=lambda x: x[1])

    return result_print(sorted_courses_and_students, courses, invalid_students)




# print(softuni_students(('id_22', 'Programmingkitten'),('id_22', 'MitkoTheDark'),
#                        ('id_22', 'Bobosa253'),('id_08', 'KrasimirAtanasov'),('id_22', 'DaniBG'),
#                        id_321='HTML & CSS',id_22='Machine Learning',id_08='JS Advanced'))

print(softuni_students(('id_22', 'Programmingkitten'),('id_11', 'MitkoTheDark'),
                       ('id_321', 'Bobosa253'),('id_08', 'KrasimirAtanasov'),('id_32', 'DaniBG'),
                       id_321='HTML & CSS',id_22='Machine Learning',id_08='JS Advanced'))

# print(softuni_students(('id_1', 'Kaloyan9905'),id_1='Python Web Framework',))
# print(softuni_students(('id_7', 'Silvester1'),('id_32', 'Katq21'),('id_7', 'The programmer'),
#                        id_76='Spring Fundamentals',id_7='Spring Advanced',))
