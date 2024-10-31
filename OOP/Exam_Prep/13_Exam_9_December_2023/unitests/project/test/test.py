from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation

class TestRailwayStation(TestCase):
    def setUp(self) -> None:
        self.station = RailwayStation("North")

    def test_constructor(self):
        self.assertEqual("North", self.station.name)
        self.assertEqual(deque([]), self.station.arrival_trains)
        self.assertEqual(deque([]), self.station.departure_trains)

    def test_name_length_with_three_symbols_edge_case_expected_exception(self): #probably a test with no letters
        with self.assertRaises(ValueError) as ve:
            self.station.name = "rtv"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_length_with_less_than_three_symbols_expected_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "rt"

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_if_train_is_added_to_the_queue(self):
        self.station.new_arrival_on_board("Chaika")
        self.assertEqual(deque(["Chaika"]), self.station.arrival_trains)

    def test_train_has_arrived_if_other_trains_have_to_arrive(self):
        self.station.arrival_trains = deque(["Varna", "Plovdiv", "Sofia"])
        result = self.station.train_has_arrived("Chaika")

        self.assertEqual("There are other trains to arrive before Chaika.", result)
        self.assertEqual(deque(["Varna", "Plovdiv", "Sofia"]),self.station.arrival_trains)

    def test_train_has_arrived_if_there_this_train_is_the_expected_one(self): #possible test withe empty arrival que
        self.station.arrival_trains = deque(["Varna", "Plovdiv", "Sofia"])
        result = self.station.train_has_arrived("Varna")

        self.assertEqual(deque(["Plovdiv", "Sofia"]), self.station.arrival_trains)
        self.assertEqual(deque(["Varna"]), self.station.departure_trains)
        self.assertEqual("Varna is on the platform and will leave in 5 minutes.", result)

    def test_train_has_left_expect_true(self):
        self.station.departure_trains = deque(["Varna", "Plovdiv", "Sofia"])
        result = self.station.train_has_left("Varna")

        self.assertEqual(deque(["Plovdiv", "Sofia"]), self.station.departure_trains)
        self.assertEqual(True, result)

    def test_train_has_left_with_an_empty_que_expect_false(self):
        result = self.station.train_has_left("Varna")

        self.assertEqual(deque([]),self.station.departure_trains)
        self.assertEqual(False, result)

    def test_train_has_left_with_another_train_in_front_of_the_departure_que_expect_false(self):
        self.station.departure_trains = deque(["Varna", "Plovdiv", "Sofia"])
        result = self.station.train_has_left("Plovdiv")

        self.assertEqual(False, result)


if __name__ == '__main__':
    main()