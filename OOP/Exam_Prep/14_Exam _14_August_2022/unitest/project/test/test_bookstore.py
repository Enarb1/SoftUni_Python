from unittest import TestCase, main
from project.bookstore import Bookstore

class TestBookstore(TestCase):
    def setUp(self):
        self.bookstore = Bookstore(100)

    def test_init(self):
        self.assertEqual(100, self.bookstore.books_limit)

    def test_total_sold_books_property(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.invalid_bookstore = Bookstore(0)
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_len_method(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 3,
            "Mira": 2,
            "Adit": 1
        }

        result = self.bookstore.__len__()
        self.assertEqual(6, result)

    def test_len_method_with_no_books(self):
        self.bookstore.availability_in_store_by_book_titles = {}
        self.assertEqual(0, len(self.bookstore))

    def test_receive_book_with_no_limit(self):
        self.bookstore.books_limit = 6
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 3,
            "Mira": 2,
            "Adit": 1
        }

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("New", 1)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_receive_book_with_new_title(self):
        self.bookstore.books_limit = 6
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 3,
        }

        result = self.bookstore.receive_book("New", 1)
        expected = "1 copies of New are available in the bookstore."

        self.assertEqual(expected, result)
        self.assertEqual(
            {
                "Branko": 3,
                "New": 1
            },
            self.bookstore.availability_in_store_by_book_titles
        )


    def test_receive_book_with_already_existing_title(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 3,
        }
        result = self.bookstore.receive_book("Branko", 1)
        expected = "4 copies of Branko are available in the bookstore."

        self.assertEqual(expected, result)
        self.assertEqual(
            {
                "Branko": 4,
            },
            self.bookstore.availability_in_store_by_book_titles
        )

    def test_receive_book_reaching_limit(self):
        self.bookstore.books_limit = 5
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3
        }
        result = self.bookstore.receive_book("Book2", 2)
        self.assertEqual("2 copies of Book2 are available in the bookstore.", result)
        self.assertEqual(5, len(self.bookstore))


    def test_sell_books_with_unavailable_title(self):
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Branko", 2)

        self.assertEqual("Book Branko doesn't exist!", str(ex.exception))

    def test_sell_books_with_already_existing_title_but_not_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 1,
        }
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Branko", 2)

        self.assertEqual("Branko has not enough copies to sell. Left: 1", str(ex.exception))

    def test_sell_books_with_enough_copies(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 3,
        }
        result = self.bookstore.sell_book("Branko", 2)
        expected = "Sold 2 copies of Branko"

        self.assertEqual({"Branko": 1}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual(expected, result)
        

    def test_str_method_with_books(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Branko": 3,
            "Mira": 2,
            "Adit": 1
        }
        self.bookstore.sell_book("Branko", 2)
        expected = ("Total sold books: 2\n"
                    "Current availability: 4\n"
                    " - Branko: 1 copies\n"
                    " - Mira: 2 copies\n"
                    " - Adit: 1 copies")
        result = self.bookstore.__str__()

        self.assertEqual(expected, result)

    def test_str_method_no_books(self):
        expected = "Total sold books: 0\nCurrent availability: 0"
        self.assertEqual(expected, str(self.bookstore))


if __name__ == '__main__':
    main()