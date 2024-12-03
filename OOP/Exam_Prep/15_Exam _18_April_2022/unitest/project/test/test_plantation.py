from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_init(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_with_already_hired_worker(self):
        self.plantation.workers = ["Branko"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Branko")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_with_new_worker(self):
        result = self.plantation.hire_worker("Branko")
        expected = "Branko successfully hired."
        self.assertEqual(["Branko"], self.plantation.workers)
        self.assertEqual(expected, result)

    def test_len_method(self):
        self.plantation.workers = ["Branko"]
        self.plantation.plants = {"Branko": ["Tulip", "Rose", "Orange"]}
        result = self.plantation.__len__()
        self.assertEqual(3, result)

    def test_planting_with_not_hired_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Branko", "Rose")
        self.assertEqual("Worker with name Branko is not hired!", str(ve.exception))

    def test_planting_with_no_more_space(self):
        self.plantation.size = 3
        self.plantation.workers = ["Branko"]
        self.plantation.plants = {"Branko": ["Tulip", "Rose", "Orange"]}
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Branko", "Kokiche")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_with_worker_that_has_planted(self):
        self.plantation.workers = ["Branko"]
        self.plantation.plants = {"Branko": ["Tulip", "Rose"]}
        result = self.plantation.planting("Branko", "Orange")
        expected = "Branko planted Orange."
        self.assertEqual({"Branko": ["Tulip", "Rose", "Orange"]}, self.plantation.plants)
        self.assertEqual(expected, result)

    def test_planting_with_worker_that_has_not_planted(self):
        self.plantation.workers = ["Branko", "Mira"]
        self.plantation.plants = {"Branko": ["Tulip", "Rose"]}
        result = self.plantation.planting("Mira", "Orange")
        expected = "Mira planted it's first Orange."
        self.assertEqual({"Branko": ["Tulip", "Rose"], "Mira": ["Orange"]}, self.plantation.plants)
        self.assertEqual(expected, result)

    def test_str_method(self):
        self.plantation.workers = ["Branko", "Mira"]
        self.plantation.plants = {"Branko": ["Tulip", "Rose"], "Mira": ["Orange"]}
        result = self.plantation.__str__()
        expected = "Plantation size: 10\nBranko, Mira\nBranko planted: Tulip, Rose\nMira planted: Orange"
        self.assertEqual(expected, result)

    def test_repr(self):
        self.plantation.workers = ["Branko", "Mira"]
        result = self.plantation.__repr__()
        expected = "Size: 10\nWorkers: Branko, Mira"
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
