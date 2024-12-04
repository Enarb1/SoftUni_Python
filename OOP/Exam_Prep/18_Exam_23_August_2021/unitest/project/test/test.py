from unittest import TestCase, main
from project.library import Library

class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library("Mira")

    def test_init(self):
        self.assertEqual("Mira", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter_expect_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_with_new_author(self):
        self.library.add_book("Branko", "Title")
        self.assertEqual({"Branko": ["Title"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author_and_new_title(self):
        self.library.books_by_authors = {"Branko": ["Title"]}
        self.library.add_book("Branko", "Mira")

        self.assertEqual({"Branko": ["Title", "Mira"]}, self.library.books_by_authors)

    def test_add_book_with_existing_author_and_title(self):
        self.library.books_by_authors = {"Branko": ["Title"]}
        self.library.add_book("Branko", "Title")

        self.assertEqual({"Branko": ["Title"]}, self.library.books_by_authors)

    def test_add_reader_with_new_reader(self):
        self.library.add_reader("Branko")
        self.assertEqual({"Branko": []}, self.library.readers)

    def test_add_reader_with_existing_reader(self):
        self.library.readers = {"Branko": []}
        result = self.library.add_reader("Branko")
        expected = "Branko is already registered in the Mira library."

        self.assertEqual(expected, result)
        self.assertEqual({"Branko": []}, self.library.readers)

    def test_rent_book_with_invalid_reader(self):
        self.library.books_by_authors = {"Branko": ["Title", "Other Title", "One more title"]}
        self.library.readers = {"Adit": []}
        result = self.library.rent_book("John", "Branko", "Title")
        expected = "John is not registered in the Mira Library."

        self.assertEqual(expected, result)
        self.assertEqual({"Branko": ["Title", "Other Title", "One more title"]}, self.library.books_by_authors)
        self.assertEqual({"Adit": []}, self.library.readers)

    def test_rent_book_with_invalid_author(self):
        self.library.books_by_authors = {"Branko": ["Title", "Other Title", "One more title"]}
        self.library.readers = {"Adit": []}
        result = self.library.rent_book("Adit", "John", "Title")
        expected = "Mira Library does not have any John's books."

        self.assertEqual(expected, result)
        self.assertEqual({"Branko": ["Title", "Other Title", "One more title"]}, self.library.books_by_authors)
        self.assertEqual({"Adit": []}, self.library.readers)

    def test_rent_book_with_unavailable_book_title(self):
        self.library.books_by_authors = {"Branko": ["Title", "Other Title", "One more title"]}
        self.library.readers = {"Adit": []}
        result = self.library.rent_book("Adit", "Branko", "John")
        expected = """Mira Library does not have Branko's "John"."""

        self.assertEqual(expected, result)
        self.assertEqual({"Branko": ["Title", "Other Title", "One more title"]}, self.library.books_by_authors)
        self.assertEqual({"Adit": []}, self.library.readers)

    def test_rent_book_with_success(self):
        self.library.books_by_authors = {"Branko": ["Title", "Other Title", "One more title"]}
        self.library.readers = {"Adit": []}
        self.library.rent_book("Adit", "Branko", "Title")

        self.assertEqual({"Adit": [{"Branko": "Title"}]},self.library.readers)
        self.assertEqual({"Branko": ["Other Title", "One more title"]}, self.library.books_by_authors)

if __name__ == '__main__':
    main()
