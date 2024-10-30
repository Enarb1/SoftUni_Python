from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot

class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot(
            "Alpine",
            "Helper",
            100,
            200)

        self.robot_with_software = ClimbingRobot(
            "Indoor",
            "Helper",
            100,
            200)

        self.robot_with_software.installed_software = [
            {"name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 49 },
            {"name": "ARS", "capacity_consumption": 49, "memory_consumption": 51 }
        ]

    def test_init(self):
        self.assertEqual("Alpine", self.robot.category)
        self.assertEqual("Helper", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(200, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_if_robot_is_with_invalid_category(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "invalid"

        self.assertEqual(f"Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']",
                         str(ve.exception))

    def test_get_used_capacity(self):
        expected_result = sum(s["capacity_consumption"] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_capacity()

        self.assertEqual(expected_result, result)

    def test_show_available_capacity(self):
        expected_result = (self.robot_with_software.capacity -
                           sum(s["capacity_consumption"] for s in self.robot_with_software.installed_software))
        result = self.robot_with_software.get_available_capacity()

        self.assertEqual(expected_result, result)

    def test_show_used_memory(self):
        expected_result = sum(s['memory_consumption'] for s in self.robot_with_software.installed_software)
        result = self.robot_with_software.get_used_memory()

        self.assertEqual(expected_result, result)

    def test_show_available_memory(self):
        expected_result = (self.robot_with_software.memory -
                           sum(s['memory_consumption'] for s in self.robot_with_software.installed_software))
        result = self.robot_with_software.get_available_memory()

        self.assertEqual(expected_result, result)

    def test_install_software_with_both_values_less_than_max_values_expect_success(self):
        result = self.robot.install_software({
            "name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 50
        })

        self.assertEqual(f"Software 'PyCharm' successfully installed on Alpine part.", result)

        self.assertEqual([{
            "name": "PyCharm", "capacity_consumption": 50, "memory_consumption": 50
        }], self.robot.installed_software)


    def test_install_software_with_both_values_equal_max_values_expect_success(self):
        result = self.robot.install_software({
            "name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200
        })

        self.assertEqual(f"Software 'PyCharm' successfully installed on Alpine part.", result)
        self.assertEqual([{
            "name": "PyCharm", "capacity_consumption": 100, "memory_consumption": 200
        }], self.robot.installed_software)

    def test_install_software_with_capacity_greater_than_the_max_value_expect_no_success(self):
        result = self.robot.install_software({
            "name": "PyCharm", "capacity_consumption": 2000, "memory_consumption": 10
        })

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Alpine part.", result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_memory_greater_than_max_value_expect_no_success(self):
        result = self.robot.install_software({
            "name": "PyCharm", "capacity_consumption": 10, "memory_consumption": 10010
        })

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Alpine part.", result)
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_both_values_greater_than_max_values_expect_no_success(self):
        result = self.robot.install_software({
            "name": "PyCharm", "capacity_consumption": 2000, "memory_consumption": 2000
        })

        self.assertEqual(f"Software 'PyCharm' cannot be installed on Alpine part.", result)
        self.assertEqual([], self.robot.installed_software)

if __name__ == '__main__':
    main()