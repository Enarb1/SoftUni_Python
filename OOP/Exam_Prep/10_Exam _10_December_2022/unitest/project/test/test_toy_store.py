from unittest import TestCase, main
from project.toy_store import ToyStore

class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_init(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_with_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('Z', "Branko")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_with_toy_already_in_shelf(self):
        self.toy_store.toy_shelf = {
            "A": "Branko",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', "Branko")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))


    def test_add_toy_with_taken_shelf(self):
        self.toy_store.toy_shelf = {
            "A": "Branko",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy('A', "Mira")

        self.assertEqual("Shelf is already taken!", str(ex.exception))


    def test_add_toy_with_valid_and_free_shelf(self):
        self.toy_store.toy_shelf = {
            "A": "Branko",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.toy_store.add_toy('B', "Mira")

        self.assertEqual(
            {
                "A": "Branko",
                "B": "Mira",
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            },
            self.toy_store.toy_shelf
        )

        self.assertEqual("Toy:Mira placed successfully!", result)


    def test_remove_toy_with_invalid_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('Z', "Branko")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))


    def test_remove_toy_with_valid_shelf_wrong_toy(self):
        self.toy_store.toy_shelf = {
            "A": "Branko",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy('A', "Mira")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


    def test_remove_toy_with_valid_shelf_and_toy(self):
        self.toy_store.toy_shelf = {
            "A": "Branko",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        result = self.toy_store.remove_toy('A', "Branko")

        self.assertEqual(
            {
                "A": None,
                "B": None,
                "C": None,
                "D": None,
                "E": None,
                "F": None,
                "G": None,
            },
            self.toy_store.toy_shelf
        )
        self.assertEqual("Remove toy:Branko successfully!", result)


if __name__ == '__main__':
    main()