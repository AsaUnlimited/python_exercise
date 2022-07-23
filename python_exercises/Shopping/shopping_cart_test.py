import unittest
from . import shopping_cart


class ShoppingCartTest(unittest.TestCase):
    def test_that_shopping_cart_can_be_created(self):
        shopping_cart1 = shopping_cart.Cart()

        self.assertIsNotNone(shopping_cart1)
        self.assertIsInstance(shopping_cart1, shopping_cart.Cart)


if __name__ == '__main__':
    unittest.main()
