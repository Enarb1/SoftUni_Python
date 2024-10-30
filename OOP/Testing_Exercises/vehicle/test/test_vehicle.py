from unittest import TestCase, main
from project.vehicle import Vehicle

class VehicleTest(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 200)

    def test_default_fuel_consumption_constant(self):
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_not_enough_exception(self): #can have a problem
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(2000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_fuel_is_enough(self):
        self.vehicle.drive(10)
        self.assertEqual(87.5, self.vehicle.fuel)


    def test_refuel_if_refuel_is_more_than_the_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1000)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_if_additional_fuel_is_less_than_or_even_capacity(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(80)
        self.assertEqual(80, self.vehicle.fuel)

    def test_string_method_return_message(self):
        expected_result = f"The vehicle has 200 " \
               f"horse power with 100 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected_result, str(self.vehicle))


if __name__ == '__main__':
    main()