from unittest import TestCase, main
# from OOP.Testing.Second_Test_Cat.cat import Cat

class TestCat(TestCase):

    def setUp(self) -> None:
        self.cat = Cat("Mira")

    def test_correct_init(self):
        self.assertEqual("Mira", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_cat_feed_makes_cat_fed_and_sleepy_and_size_increase_1(self):
        expected_size = self.cat.size + 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_is_fed_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_cat_goes_to_sleep_and_is_not_sleepy(self):
        self.cat.sleepy = True
        self.cat.fed = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


    def test_is_sleepy_exception(self):
        self.cat.fed = False

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))



if __name__ == '__main__':
    main()