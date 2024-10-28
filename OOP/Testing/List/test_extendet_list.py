from unittest import TestCase, main
# from OOP.Testing.List.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self) -> None:
        self.i_list = IntegerList(5.5, 5, 4, 3, 1, "hello")

    def test_correct_integer_list(self):
        self.assertEqual([5, 4, 3, 1], self.i_list.get_data())

    def test_add_element_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_append_element(self):
        expected_list = self.i_list.get_data() + [4]

        self.i_list.add(4)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_remove_with_invalid_index_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(10000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_element_from_valid_index_in_list(self):
        self.i_list.remove_index(0)

        self.assertEqual([4, 3, 1], self.i_list.get_data())

    def test_get_invalid_index_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.get(10000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_element_from_valid_index_in_list(self):
        result = self.i_list.get(0)
        self.assertEqual(5, result)

    def test_insert_on_invalid_index_exception(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(10000, 6)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_invalid_type_element_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(0, 6.6)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_insert_valid_element_on_valid_index_in_list(self):
        expected_list = self.i_list.get_data().copy()

        expected_list.insert(0, 6)
        self.i_list.insert(0, 6)

        self.assertEqual(expected_list, self.i_list.get_data())

    def test_biggest_num(self):
        result = self.i_list.get_biggest()
        self.assertEqual(5, result)

    def test_get_index_get_element_from_index(self):
        result = self.i_list.get_index(5)
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
