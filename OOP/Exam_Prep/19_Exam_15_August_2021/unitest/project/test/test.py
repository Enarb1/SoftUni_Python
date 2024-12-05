from unittest import TestCase, main
from project.pet_shop import PetShop

class TestPetShop(TestCase):
    def setUp(self):
        self.pet_shop = PetShop("Adit")

    def test_init(self):
        self.assertEqual("Adit", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_invalid_qty(self):
        with self.assertRaises(ValueError) as ve:
            self.pet_shop.add_food("Meat", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_food_with_new_food(self):
        result = self.pet_shop.add_food("Meat", 10)
        expected = "Successfully added 10.00 grams of Meat."

        self.assertEqual(expected, result)
        self.assertEqual({"Meat": 10}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_with_existing_food(self):
        self.pet_shop.food = {"Meat": 10}
        result = self.pet_shop.add_food("Meat", 10)
        expected = "Successfully added 10.00 grams of Meat."

        self.assertEqual(expected, result)
        self.assertEqual({"Meat": 20}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_pet_with_new_name(self):
        result = self.pet_shop.add_pet("Adit")
        expected = "Successfully added Adit."

        self.assertEqual(expected, result)
        self.assertEqual(["Adit"], self.pet_shop.pets)
        self.assertEqual({}, self.pet_shop.food)

    def test_add_pet_with_existing_name(self):
        self.pet_shop.pets = ["Adit"]
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Adit")
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_with_invalid_pet(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("Meat", "Adit")
        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_with_invalid_food(self):
        self.pet_shop.pets = ["Adit"]
        result = self.pet_shop.feed_pet("Meat", "Adit")
        expected = 'You do not have Meat'

        self.assertEqual(expected, result)

    def test_feed_pet_with_not_enough_food(self):
        self.pet_shop.pets = ["Adit"]
        self.pet_shop.food = {"Meat": 10}
        result = self.pet_shop.feed_pet("Meat", "Adit")
        expected = "Adding food..."

        self.assertEqual(expected, result)
        self.assertEqual({"Meat": 1010.00}, self.pet_shop.food)

    def test_feed_pet_with_enough_food(self):
        self.pet_shop.pets = ["Adit"]
        self.pet_shop.food = {"Meat": 100}
        result = self.pet_shop.feed_pet("Meat", "Adit")
        expected = "Adit was successfully fed"

        self.assertEqual(expected, result)
        self.assertEqual({"Meat": 0}, self.pet_shop.food)

    def test_repr(self):
        self.pet_shop.pets = ["Adit", "Branko", "Mira", "Kara"]
        expected = 'Shop Adit:\n'\
                   'Pets: Adit, Branko, Mira, Kara'

        self.assertEqual(expected, repr(self.pet_shop))


if __name__ == '__main__':
    main()
