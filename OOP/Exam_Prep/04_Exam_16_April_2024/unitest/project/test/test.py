from unittest import TestCase, main
from project.restaurant import Restaurant


class TestRestaurant(TestCase):
    def setUp(self) -> None:
        self.restaurant = Restaurant("Mira", 4)

    def test_init(self):
        self.assertEqual("Mira", self.restaurant.name)
        self.assertEqual(4, self.restaurant.capacity)
        self.assertEqual([], self.restaurant.waiters)

    def test_name_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ''

        self.assertEqual("Invalid name!", str(ve.exception))

    def test_capacity_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1

        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_get_waiters_with_no_min_and_max_earnings(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Charlie', 'total_earnings': 1500},
            {'name': 'Dana', 'total_earnings': 700},
        ]

        result = self.restaurant.get_waiters()

        self.assertEqual([
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Charlie', 'total_earnings': 1500},
            {'name': 'Dana', 'total_earnings': 700},
        ], result)


    def test_get_waiters_only_with_min_earnings_set(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Charlie', 'total_earnings': 1500},
            {'name': 'Dana', 'total_earnings': 700},
        ]

        result = self.restaurant.get_waiters(1000, None)

        self.assertEqual([
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Charlie', 'total_earnings': 1500},
        ], result)

    def test_get_waiters_only_with_max_earnings_set(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Charlie', 'total_earnings': 1500},
            {'name': 'Dana', 'total_earnings': 700},
        ]

        result = self.restaurant.get_waiters(None, 1000)

        self.assertEqual([
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Dana', 'total_earnings': 700},
        ], result)

    def test_get_waiters_with_min_and_max_earnings_set(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Charlie', 'total_earnings': 1500},
            {'name': 'Dana', 'total_earnings': 700},
        ]

        result = self.restaurant.get_waiters(800, 1200)
        self.assertEqual([
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
        ], result)

    def test_add_waiter_with_no_space_left(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Charlie', 'total_earnings': 1500},
            {'name': 'Dana', 'total_earnings': 700},
        ]

        result = self.restaurant.add_waiter("Branko")

        self.assertEqual("No more places!", result)

    def test_add_waiter_with_existing_waiter(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
        ]

        result = self.restaurant.add_waiter("Bob")

        self.assertEqual("The waiter Bob already exists!", result)

    def test_add_waiter_expect_added_waiter(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
        ]

        result = self.restaurant.add_waiter("Branko")

        self.assertEqual([
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
            {'name': 'Branko'}
        ], self.restaurant.waiters)

        self.assertEqual("The waiter Branko has been added.", result)

    def test_remove_waiter_expect_removed_waiter(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
        ]

        result = self.restaurant.remove_waiter("Bob")

        self.assertEqual([{'name': 'Alice', 'total_earnings': 1200},], self.restaurant.waiters)
        self.assertEqual("The waiter Bob has been removed.", result)

    def test_remove_waiter_with_non_existent_waiter(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
        ]

        result = self.restaurant.remove_waiter("Branko")

        self.assertEqual("No waiter found with the name Branko.", result)

    def test_sum_waiters_total_earnings(self):
        self.restaurant.waiters = [
            {'name': 'Alice', 'total_earnings': 1200},
            {'name': 'Bob', 'total_earnings': 800},
        ]

        result = self.restaurant.get_total_earnings()

        self.assertEqual(2000, result)

if __name__ == '__main__':
    main()
