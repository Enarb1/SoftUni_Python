from unittest import TestCase, main
from project.trip import Trip

class TestTrip(TestCase):
    def setUp(self) -> None:
        self.trip = Trip(
            10000.00,
            2,
            True
            )

    def test_init(self):
        self.assertEqual(10000.00, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertEqual(True, self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_setter_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_setter_with_less_than_two_travelers(self):
        self.trip.travelers = 1
        self.trip.is_family = True
        self.assertFalse(self.trip.is_family)

    def test_is_family_setter_with_more_than_one_travelers(self):
        self.trip.travelers = 2
        self.trip.is_family = True
        self.assertTrue(self.trip.is_family)

    def test_is_family_setter_with_one_traveler_and_is_family_set_to_false(self):
        self.trip.travelers = 1
        self.trip.is_family = False
        self.assertFalse(self.trip.is_family)

    def test_book_a_trip_with_invalid_destination(self):
        result = self.trip.book_a_trip("Congo")
        self.assertEqual(
            'This destination is not in our offers, please choose a new one!',
            result
        )

    def test_book_a_trip_with_valid_destination_and_is_family_false(self):
        self.trip.is_family = False
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual({"Bulgaria": 1000}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(9000.00, self.trip.budget)
        self.assertEqual(
            "Successfully booked destination Bulgaria! Your budget left is 9000.00",
            result
        )

    def test_book_a_trip_with_valid_destination_and_is_family_true(self):
        self.trip.is_family = True
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual({"Bulgaria": 900}, self.trip.booked_destinations_paid_amounts)
        self.assertEqual(9100.00, self.trip.budget)
        self.assertEqual(
            "Successfully booked destination Bulgaria! Your budget left is 9100.00",
            result
        )

    def test_book_a_trip_with_valid_destination_and_not_enough_budget(self):
        self.trip.travelers = 50
        self.trip.is_family = False
        result = self.trip.book_a_trip("Bulgaria")

        self.assertEqual('Your budget is not enough!', result)

    def test_booking_status_without_bookings(self):
        result = self.trip.booking_status()
        self.assertEqual("No bookings yet. Budget: 10000.00", result)

    def test_booking_status_with_bookings(self):
        self.trip.budget = 35_800.00
        self.trip.travelers = 1
        self.trip.is_family = False
        self.trip.booked_destinations_paid_amounts = {
            "Bulgaria": 500,
            'New Zealand': 7500,
            'Brazil': 6200
        }

        expected = """Booked Destination: Brazil
Paid Amount: 6200.00
Booked Destination: Bulgaria
Paid Amount: 500.00
Booked Destination: New Zealand
Paid Amount: 7500.00
Number of Travelers: 1
Budget Left: 35800.00"""

        result = self.trip.booking_status()
        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
