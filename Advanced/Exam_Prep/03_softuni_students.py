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