from unittest import TestCase,main
from project.senior_student import SeniorStudent

class TestSeniorStudent(TestCase):
    def setUp(self):
        self.student = SeniorStudent(
            "1234",
            "Branko",
            2.0
        )

    def test_init(self):
        self.assertEqual("1234", self.student.student_id)
        self.assertEqual("Branko", self.student.name)
        self.assertEqual(2.0, self.student.student_gpa)
        self.assertEqual(set(), self.student.colleges)

    def test_student_id_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ve.exception))

    def test_name_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student.name = " "
        self.assertEqual("Student name cannot be null or empty!", str(ve.exception))

    def test_student_gpa_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))

    def test_apply_to_college_with_not_enough_gpa(self):
        result = self.student.apply_to_college(2.1, "Harvard")
        expected = 'Application failed!'

        self.assertEqual(expected, result)

    def test_apply_to_college_with_enough_gpa(self):
        result = self.student.apply_to_college(1.5, "Harvard")
        expected = 'Branko successfully applied to Harvard.'

        self.assertEqual(expected, result)
        self.assertEqual({'HARVARD'}, self.student.colleges)

    def test_update_gpa_with_invalid_amount(self):
        result = self.student.update_gpa(1.0)
        expected = 'The GPA has not been changed!'

        self.assertEqual(expected, result)
        self.assertEqual(2.0, self.student.student_gpa)

    def test_update_gpa_with_valid_amount(self):
        result = self.student.update_gpa(3.0)
        expected = 'Student GPA was successfully updated.'

        self.assertEqual(expected, result)
        self.assertEqual(3.0, self.student.student_gpa)

    def test_eq_expect_true(self):
        self.other = SeniorStudent(
            "1111",
            "Mira",
            2.0
        )

        self.assertTrue(self.student.__eq__(self.other))

    def test_eq_expect_false(self):
        self.other = SeniorStudent(
            "1111",
            "Mira",
            3.0
        )

        self.assertFalse(self.student.__eq__(self.other))

if __name__ == '__main__':
    main()