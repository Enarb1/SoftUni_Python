from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar(
            "Swift",
            "Combi",
            1000,
            5000
        )

        self.car2 = SecondHandCar(
            "Toyota",
            "Pick-up",
            2000,
            10000
        )


    def test_init(self):
        self.assertEqual("Swift", self.car.model)
        self.assertEqual("Combi", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(5000, self.car.price)
        self.assertEqual([], self.car.repairs)


    def test_price_value_setter_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 0.99

        self.assertEqual('Price should be greater than 1.0!',str(ve.exception))


    def test_car_mileage_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 99

        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',str(ve.exception))


    def test_promo_price_with_higher_price_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(10000)

        self.assertEqual('You are supposed to decrease the price!',str(ve.exception))


    def test_promo_price_with_lower_price_expect_success(self):
        result = self.car.set_promotional_price(1000)

        self.assertEqual(1000, self.car.price)
        self.assertEqual('The promotional price has been successfully set.', result)


    def test_need_repair_with_a_higher_price_expect_impossible_msg_return(self):
        expected_msg = 'Repair is impossible!'
        result = self.car.need_repair(4000.0, "engine repair")

        self.assertEqual(expected_msg, result)


    def test_need_repair_with_a_lower_price_expect_updated_price_updated_repair_list_msg(self):
        expected_msg = 'Price has been increased due to repair charges.'
        result = self.car.need_repair(1000, "Engine repair")

        self.assertEqual(6000, self.car.price)
        self.assertEqual(["Engine repair"], self.car.repairs)
        self.assertEqual(expected_msg, result)


    def test_gt_method_with_different_car_types(self):
        expected_msg = 'Cars cannot be compared. Type mismatch!'
        result = self.car.__gt__(self.car2)

        self.assertEqual(expected_msg, result)


    def test_gt_method_with_same_car_type_and_higher_price_expect_true(self):
        self.car.car_type = "Combi"
        self.car2.price = 1000

        self.assertTrue(self.car.__gt__(self.car2))


    def test_gt_method_with_same_car_type_and_lower_price_expect_false(self):
        self.car2.car_type = "Combi"

        self.assertFalse(self.car.__gt__(self.car2))


    def test_str_method(self):
        expected = ("Model Swift | Type Combi | Milage 1000km\n"
                    "Current price: 5000.00 | Number of Repairs: 0")

        self.assertEqual(self.car.__str__(), expected)


if __name__ == '__main__':
    main()