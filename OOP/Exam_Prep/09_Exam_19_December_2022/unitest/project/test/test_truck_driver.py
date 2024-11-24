from unittest import TestCase, main
from project.truck_driver import TruckDriver

class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Branko", 10.0)

    def test_init(self):
        self.assertEqual("Branko", self.driver.name)
        self.assertEqual(10.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)


    def test_earned_monet_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Branko went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_with_already_added_location_expect_exception(self):
        self.driver.available_cargos = {"Sofia": 20}
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 10)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))


    def test_add_cargo_offer_with_not_added_location_expect_success(self):
        result = self.driver.add_cargo_offer("Sofia", 10)
        expected = "Cargo for 10 to Sofia was added as an offer."

        self.assertEqual(expected, result)
        self.assertEqual({"Sofia": 10}, self.driver.available_cargos)

    def test_drive_best_cargo_offer_without_cargo(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_with_available_cargo_and_eat(self):
        self.driver.available_cargos = {"Sofia": 350, "Plovdiv": 150, "Varna": 3}
        result = self.driver.drive_best_cargo_offer()
        expected_msg = "Branko is driving 350 to Sofia."
        earned = self.driver.available_cargos["Sofia"] * self.driver.money_per_mile
        expenses = ((20 * (self.driver.available_cargos["Sofia"] // 250))
                    + (45 * (self.driver.available_cargos["Sofia"] // 1000))
                    + (500 * (self.driver.available_cargos["Sofia"] // 1500))
                    + (7500 * (self.driver.available_cargos["Sofia"] // 10000)))

        money = earned - expenses

        self.assertEqual(money, self.driver.earned_money)
        self.assertEqual(350, self.driver.miles)
        self.assertEqual(expected_msg, result)


    def test_drive_best_cargo_offer_with_cargo_eat_sleep(self):
        self.driver.available_cargos = {"Sofia": 1100}
        result = self.driver.drive_best_cargo_offer()
        expected_msg = "Branko is driving 1100 to Sofia."
        earned = self.driver.available_cargos["Sofia"] * self.driver.money_per_mile
        expenses = ((20 * (self.driver.available_cargos["Sofia"] // 250))
                    + (45 * (self.driver.available_cargos["Sofia"] // 1000))
                    + (500 * (self.driver.available_cargos["Sofia"] // 1500))
                    + (7500 * (self.driver.available_cargos["Sofia"] // 10000)))

        money = earned - expenses

        self.assertEqual(money, self.driver.earned_money)
        self.assertEqual(1100, self.driver.miles)
        self.assertEqual(expected_msg, result)


    def test_drive_best_cargo_with_added_cargo_eat_sleep_pump_gas(self):
        self.driver.available_cargos = {"Sofia": 1505}
        result = self.driver.drive_best_cargo_offer()
        expected_msg = "Branko is driving 1505 to Sofia."
        earned = self.driver.available_cargos["Sofia"] * self.driver.money_per_mile
        expenses = ((20 * (self.driver.available_cargos["Sofia"] // 250))
                    + (45 * (self.driver.available_cargos["Sofia"] // 1000))
                    + (500 * (self.driver.available_cargos["Sofia"] // 1500))
                    + (7500 * (self.driver.available_cargos["Sofia"] // 10000)))

        money = earned - expenses

        self.assertEqual(money, self.driver.earned_money)
        self.assertEqual(1505, self.driver.miles)
        self.assertEqual(expected_msg, result)


    def test_drive_best_cargo_with_added_cargo_eat_sleep_pump_gas_repair(self):
        self.driver.available_cargos = {"Sofia": 7505}
        result = self.driver.drive_best_cargo_offer()
        expected_msg = "Branko is driving 7505 to Sofia."
        earned = self.driver.available_cargos["Sofia"] * self.driver.money_per_mile
        expenses = ((20 * (self.driver.available_cargos["Sofia"] // 250))
                    + (45 * (self.driver.available_cargos["Sofia"] // 1000))
                    + (500 * (self.driver.available_cargos["Sofia"] // 1500))
                    + (7500 * (self.driver.available_cargos["Sofia"] // 10000)))

        money = earned - expenses

        self.assertEqual(money, self.driver.earned_money)
        self.assertEqual(7505, self.driver.miles)
        self.assertEqual(expected_msg, result)


    def test_drive_best_cargo_offer_with_added_cargo_but_going_bankrupt(self):
        self.driver.money_per_mile = 0.001
        self.driver.available_cargos = {"Sofia": 300}
        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual("Branko went bankrupt.", str(ve.exception))

    def test_check_for_activities(self):
        self.driver.available_cargos = {"Sofia": 250}
        self.driver.drive_best_cargo_offer()

        self.assertEqual(2480, self.driver.earned_money)


    def test_eat(self):
        self.driver.earned_money = 100

        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(60, self.driver.earned_money)

    def test_sleep(self):
        self.driver.earned_money = 100

        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(10, self.driver.earned_money)


    def test_pump_gas(self):
        self.driver.earned_money = 2000

        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)

        self.assertEqual(1000, self.driver.earned_money)


    def test_repair_truck(self):
        self.driver.earned_money = 16000

        self.driver.repair_truck(10000)
        self.driver.repair_truck(20000)

        self.assertEqual(1000, self.driver.earned_money)

    def test_repr_method(self):
        result = self.driver.__repr__()
        expected_msg = "Branko has 0 miles behind his back."

        self.assertEqual(expected_msg, result)

if __name__ == '__main__':
    main()