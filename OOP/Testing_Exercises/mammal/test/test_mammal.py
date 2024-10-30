from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Adit", "Dog", "woof")

    def test_init(self):
        self.assertEqual("Adit", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("woof", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_return_message(self):
        self.assertEqual("Adit makes woof", self.mammal.make_sound())

    def test_get_kingdom_name(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_message(self):
        self.assertEqual(f"Adit is of type Dog", self.mammal.info())


if __name__ == '__main__':
    main()