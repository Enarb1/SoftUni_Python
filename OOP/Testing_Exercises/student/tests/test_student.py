from unittest import TestCase, main
from project.student import Student

class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Branko")
        self.second_student = Student("Mira", {"Python": ["x + y = z"]})

    def test_init(self):
        self.assertEqual("Branko", self.student.name)
        self.assertEqual("Mira", self.second_student.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Python": ["x + y = z"]}, self.second_student.courses)

    def test_appending_notes_to_an_existing_course_and_return_message(self):
        expected_message = "Course already added. Notes have been updated."
        expected_course_notes = ["x + y = z", "str", "int"]

        result = self.second_student.enroll("Python", ["str", "int"])

        self.assertEqual(expected_message, result)
        self.assertEqual(expected_course_notes, self.second_student.courses["Python"])

    def test_add_new_course_with_add_course_notes_y_and_empty(self):
        result_one = self.student.enroll("Python", ["str", "int"], "Y")
        result_two = self.second_student.enroll("math", ["x", "y"])

        expected_message = "Course and course notes have been added."
        expected_student_courses = {"Python": ["str", "int"]}
        expected_second_student_courses = {"Python": ["x + y = z"], "math": ["x", "y"]}


        self.assertEqual(expected_message, result_one)
        self.assertEqual(expected_message, result_two)

        self.assertEqual(expected_student_courses, self.student.courses)
        self.assertEqual(expected_second_student_courses, self.second_student.courses)

    def test_enroll_new_course_without_notes(self):
        result = self.student.enroll("Python", ["str", "int"], "something")

        expected_message = "Course has been added."
        expected_student_courses = {"Python": []}

        self.assertEqual(expected_message, result)
        self.assertEqual(expected_student_courses, self.student.courses)

    def test_adding_notes_to_an_existing_course_and_return_message(self):
        result = self.second_student.add_notes("Python", "OOP")

        expected_message = "Notes have been updated"
        expected_course_notes = ["x + y = z", "OOP"]

        self.assertEqual(expected_message, result)
        self.assertEqual(expected_course_notes, self.second_student.courses["Python"])

    def test_adding_notes_to_a_not_existing_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python", "OOP")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_an_existing_course_and_return_message(self):
        result = self.second_student.leave_course("Python")
        expected_message = "Course has been removed"
        expected_courses = {}

        self.assertEqual(expected_message, result)
        self.assertEqual(expected_courses, self.second_student.courses)

    def test_leave_an_not_existing_course_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

if __name__ == '__main__':
    main()