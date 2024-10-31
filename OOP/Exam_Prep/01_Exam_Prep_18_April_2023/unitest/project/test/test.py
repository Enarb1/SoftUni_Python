from unittest import TestCase,main
from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']
    PRICE_INCREMENT = 1.5

    def setUp(self):
       self.my_robot = Robot(
           "001",
           "Military",
           100,
           100.00)

    def test_constructor(self):
        self.assertEqual("001", self.my_robot.robot_id)
        self.assertEqual("Military", self.my_robot.category)
        self.assertEqual(100, self.my_robot.available_capacity)
        self.assertEqual(100.00, self.my_robot.price)
        self.assertEqual([], self.my_robot.hardware_upgrades)
        self.assertEqual([], self.my_robot.software_updates)

    def test_category_if_in_allowed_categories_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.my_robot.category = "Sofia"

        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_price_attribute_if_is_less_than_zero_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.my_robot.price = -1

        self.assertEqual("Price cannot be negative!" , str(ve.exception))

    def test_upgrade_with_hardware_already_installed_expect_return_message(self):
        self.my_robot.hardware_upgrades = ["RAM", "Hard drive", "Cable"]
        result = self.my_robot.upgrade("RAM", 20.50)
        expected_message = "Robot 001 was not upgraded."

        self.assertEqual(expected_message, result)
        self.assertEqual(["RAM", "Hard drive", "Cable"], self.my_robot.hardware_upgrades)

    def test_upgrade_hardware_expect_return_message_and_updated_hardware_list_and_price(self):
        expected_message = "Robot 001 was upgraded with RAM."
        expected_price = self.my_robot.price + (10 * self.PRICE_INCREMENT)
        expected_list = ["RAM"]
        result = self.my_robot.upgrade("RAM", 10)

        self.assertEqual(expected_message, result)
        self.assertEqual(expected_price, self.my_robot.price)
        self.assertEqual(expected_list, self.my_robot.hardware_upgrades)

    def test_software_update_with_version_lower_than_the_installed(self):
        self.my_robot.software_updates = [10, 20, 30]
        expected_message = "Robot 001 was not updated."
        result =  self.my_robot.update( 20, 50)

        self.assertEqual(expected_message, result)
        self.assertEqual([10, 20, 30], self.my_robot.software_updates)
        self.assertEqual(100, self.my_robot.available_capacity)

    def test_software_update_with_bigger_version_and_no_capacity(self):
        self.my_robot.software_updates = [10, 20, 30]
        expected_message = "Robot 001 was not updated."
        result = self.my_robot.update( 50, 101)

        self.assertEqual(expected_message, result)
        self.assertEqual([10, 20, 30], self.my_robot.software_updates)
        self.assertEqual(100, self.my_robot.available_capacity)

    def test_software_update_expect_success(self):
        self.my_robot.software_updates = [10, 20, 30]
        expected_message = "Robot 001 was updated to version 50."
        result = self.my_robot.update( 50, 90)

        self.assertEqual(expected_message, result)
        self.assertEqual([10, 20, 30, 50], self.my_robot.software_updates)
        self.assertEqual(10, self.my_robot.available_capacity)

    def test_compare_robot_prices(self):
        robot_less = Robot("002", "Military", 100, 90.00)
        robot_equal = Robot("003", "Military", 100, 100.00)
        robot_greater = Robot("004", "Military", 100, 190.00)

        result = self.my_robot.__gt__(robot_less)
        self.assertEqual(
            f"Robot with ID {self.my_robot.robot_id} is more expensive than "
            f"Robot with ID {robot_less.robot_id}.", result
        )

        result = self.my_robot.__gt__(robot_equal)
        self.assertEqual(
            f"Robot with ID {self.my_robot.robot_id} costs equal to "
            f"Robot with ID {robot_equal.robot_id}.", result
        )

        result = self.my_robot.__gt__(robot_greater)
        self.assertEqual(
            f"Robot with ID {self.my_robot.robot_id} is cheaper than "
            f"Robot with ID {robot_greater.robot_id}.", result
        )


if __name__ == '__main__':
    main()