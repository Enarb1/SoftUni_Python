from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.first_shopping_cart = ShoppingCart(
            "FirstShop",
            100
        )

        self.other_shopping_cart = ShoppingCart(
            "OtherShop",
            100
        )

    def test_init(self):
        self.assertEqual("FirstShop",self.first_shopping_cart.shop_name)
        self.assertEqual(100, self.first_shopping_cart.budget)

    def test_shop_name_setter_expect_exception_with_not_upper_first_letter(self):
        expected = "Shop must contain only letters and must start with capital letter!"
        with self.assertRaises(ValueError) as ve:
            self.first_shopping_cart.shop_name = "firstShop"

        self.assertEqual(expected, str(ve.exception))

    def test_shop_name_setter_expect_exception_with_digit(self):
        expected = "Shop must contain only letters and must start with capital letter!"
        with self.assertRaises(ValueError) as ve:
            self.first_shopping_cart.shop_name = "F1rstShop"

        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_with_higher_price_expect_value_error(self):
        expected = "Product Bike cost too much!"
        with self.assertRaises(ValueError) as ve:
            self.first_shopping_cart.add_to_cart("Bike", 100.0)

        self.assertEqual(expected, str(ve.exception))

    def test_add_to_cart_with_affordable_product(self):
        expected = "Bike product was successfully added to the cart!"
        result = self.first_shopping_cart.add_to_cart("Bike", 99)

        self.assertEqual({"Bike": 99.0}, self.first_shopping_cart.products)
        self.assertEqual(expected,result)

    def test_remove_from_cart_with_product_to_remove(self):
        self.first_shopping_cart.products = {
            "Bike": 99.0,
            "Board": 50.0
        }
        expected = "Product Bike was successfully removed from the cart!"
        result = self.first_shopping_cart.remove_from_cart("Bike")

        self.assertEqual({"Board": 50.0}, self.first_shopping_cart.products)
        self.assertEqual(expected, result)

    def test_remove_from_cart_with_no_available_product_to_remove(self):
        expected = "No product with name Bike in the cart!"
        with self.assertRaises(ValueError) as ve:
            self.first_shopping_cart.remove_from_cart("Bike")

        self.assertEqual(expected, str(ve.exception))

    def test_add_magic_method(self):
        self.first_shopping_cart.products = {"Bike": 99.0}
        self.other_shopping_cart.add_to_cart("Board", 50.0)

        new_shop = self.first_shopping_cart + self.other_shopping_cart

        self.assertEqual("FirstShopOtherShop", new_shop.shop_name)
        self.assertEqual(200.0, new_shop.budget)
        self.assertEqual({
            "Bike": 99.0,
            "Board": 50.0
        }, new_shop.products)


    def test_buy_product_with_not_enough_money(self):
        self.first_shopping_cart.products = {
            "Bike": 90.0,
            "Board": 11.0
        }
        expected = "Not enough money to buy the products! Over budget with 1.00lv!"

        with self.assertRaises(ValueError) as ve:
            self.first_shopping_cart.buy_products()

        self.assertEqual(expected, str(ve.exception))

    def test_buy_product_with_enough_money(self):
        self.first_shopping_cart.products = {
            "Bike": 40.0,
            "Board": 10.0
        }
        result = self.first_shopping_cart.buy_products()
        expected = 'Products were successfully bought! Total cost: 50.00lv.'

        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()