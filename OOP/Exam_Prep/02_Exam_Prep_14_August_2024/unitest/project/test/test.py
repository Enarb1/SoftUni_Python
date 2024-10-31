from unittest import TestCase,main
from project.furniture import Furniture

class TestFurniture(TestCase):
    def setUp(self) -> None:
        self.furniture = Furniture(
            "Chair",
            100.00,
            (10, 20, 30),
            True,
            20.00)

    def test_init(self):
        self.assertEqual("Chair", self.furniture.model)
        self.assertEqual(100.00, self.furniture.price)
        self.assertEqual((10, 20, 30), self.furniture.dimensions)
        self.assertEqual(True, self.furniture.in_stock)
        self.assertEqual(20.00, self.furniture.weight)

    def test_model_name_with_empty_value_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = ""

        self.assertEqual(
            "Model must be a non-empty string with a "
            "maximum length of 50 characters.",
            str(ve.exception)
        )

    def test_model_name_with_more_than_50_characters_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = ("lkaskdaklsldlksadkldsakladslklkdaskladskldaslkldkaslkad"
                                    "skladslkadskladskllkadskladslkasdlkldsak")

        self.assertEqual(
            "Model must be a non-empty string with a "
            "maximum length of 50 characters.",
            str(ve.exception)
        )

    def test_price_with_value_less_than_zero_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.price = -1

        self.assertEqual("Price must be a non-negative number.", str(ve.exception))

    def test_dimension_values_count_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2)

        self.assertEqual("Dimensions tuple must contain 3 integers.", str(ve.exception))

    def test_dimension_values_if_all_greater_than_zero_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (0, 2, 3)

        self.assertEqual(
            "Dimensions tuple must contain integers greater than zero.",
            str(ve.exception)
        )

    def test_weight_value_with_negative_number_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = -1

        self.assertEqual("Weight must be greater than zero.", str(ve.exception))

    def test_get_available_furniture_if_model_is_available(self):
        result = self.furniture.get_available_status()
        expected_result = f"Model: {self.furniture.model} is currently in stock."

        self.assertEqual(expected_result, result)

    def test_get_available_furniture_if_model_is_unavailable(self):
        self.furniture.in_stock = False
        result = self.furniture.get_available_status()
        expected_result = f"Model: {self.furniture.model} is currently unavailable."

        self.assertEqual(expected_result, result)

    def test_get_specifications_with_weight(self):
        expected_result = "Model: Chair has the following dimensions: " \
                "10mm x 20mm x 30mm and weighs: 20.0"
        result = self.furniture.get_specifications()

        self.assertEqual(expected_result, result)

    def test_get_specifications_without_weight(self):
        self.furniture.weight = None
        expected_result = "Model: Chair has the following dimensions: " \
                          "10mm x 20mm x 30mm and weighs: N/A"
        result = self.furniture.get_specifications()

        self.assertEqual(expected_result, result)

if __name__ == '__main__':
    main()
