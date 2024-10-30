from unittest import TestCase, main
from OOP.Testing.CarManager.car_manager import Car

class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Toyota", "Corolla", 5, 40)

    def test_correct_init(self):
        self.assertEqual("Toyota", self.car.make)
        self.assertEqual("Corolla", self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(40, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)


    def test_make_with_no_value_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_with_no_value_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_with_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_with_less_than_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_with_zero_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_capacity(self):
        self.car.fuel_capacity = 80
        self.car.refuel(100)
        self.assertEqual(80, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_fuel_after_drive(self):
        self.car.refuel(100)
        self.car.drive(10)
        self.assertEqual(39.5, self.car.fuel_amount)

if __name__ == '__main__':
    main()