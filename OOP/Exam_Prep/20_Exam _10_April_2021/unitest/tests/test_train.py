from unittest import TestCase, main
from project.train.train import Train

class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("Chaika", 100)

    def test_init(self):
        self.assertEqual("Chaika", self.train.name)
        self.assertEqual(100, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_with_no_capacity_left(self):
        self.train.capacity = 1
        self.train.passengers = ["Mira"]
        with self.assertRaises(ValueError) as ve:
            self.train.add('Branko')
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_with_passenger_already_on_train(self):
        self.train.passengers = ["Mira"]
        with self.assertRaises(ValueError) as ve:
            self.train.add('Mira')
        self.assertEqual("Passenger Mira Exists", str(ve.exception))

    def test_add_with_success(self):
        result = self.train.add("Mira")
        expected = "Added passenger Mira"

        self.assertEqual(["Mira"], self.train.passengers)
        self.assertEqual(expected, result)

    def test_remove_passenger_with_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Mira")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_remove_passenger_with_success(self):
        self.train.add("Mira")
        result = self.train.remove("Mira")
        expected = "Removed Mira"

        self.assertEqual(expected, result)
        self.assertEqual([], self.train.passengers)

if __name__ == '__main__':
    main()