from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self):
        self.student = StudentReportCard("Branko", 10)

    def test_init(self):
        self.assertEqual("Branko", self.student.student_name)
        self.assertEqual(10, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_student_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(ve.exception))

    def test_school_year_setter_with_less_than_1(self):
        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_school_year_setter_with_more_than_12(self):
        with self.assertRaises(ValueError) as ve:
            self.student.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(ve.exception))

    def test_add_grade_with_new_subject(self):
        self.student.add_grade("Math", 6)
        self.assertEqual({"Math": [6]}, self.student.grades_by_subject)

    def test_add_grade_with_existing_subject(self):
        self.student.add_grade("Math", 6)
        self.student.add_grade("Math", 3)

        self.assertEqual({"Math": [6, 3]}, self.student.grades_by_subject)

    def test_add_grade_with_boundary_values(self):
        self.student.add_grade("Math", 0.0)
        self.student.add_grade("Math", 100.0)
        self.assertEqual({"Math": [0.0, 100.0]}, self.student.grades_by_subject)

    def test_average_grade_by_subject(self):
        self.student.add_grade("Math", 6)
        self.student.add_grade("Math", 3)
        self.student.add_grade("English", 6)
        self.student.add_grade("English", 3)
        self.student.add_grade("English", 3)
        result = self.student.average_grade_by_subject()
        expected = "Math: 4.50\nEnglish: 4.00"

        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects(self):
        self.student.add_grade("Math", 6)
        self.student.add_grade("Math", 3)
        self.student.add_grade("English", 6)
        self.student.add_grade("English", 3)
        self.student.add_grade("English", 3)
        result = self.student.average_grade_for_all_subjects()
        expected = "Average Grade: 4.20"

        self.assertEqual(expected, result)

    def test_repr_method(self):
        self.student.add_grade("Math", 6)
        self.student.add_grade("Math", 3)
        self.student.add_grade("English", 6)
        expected = "Name: Branko\n" \
                 "Year: 10\n" \
                 "----------\n" \
                 "Math: 4.50\nEnglish: 6.00\n" \
                 f"----------\n" \
                 f"Average Grade: 5.00"

        self.assertEqual(expected,repr(self.student))


if __name__ == '__main__':
    main()