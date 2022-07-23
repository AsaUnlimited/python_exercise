import unittest
from . import account


class AccountTest(unittest.TestCase):
    def test_account_can_be_created(self):
        account1 = account.Account("Asa")

        self.assertIsNotNone(account1)
        self.assertIsInstance(account1, account.Account)

    def test_that_account_has_a_name(self):
        """

        GIVEN   an account class
        WHEN    when a class is made
        THEN    account balance should reflect
        :return:
        """

        account1 = account.Account("Asa")
        name = account1.name
        self.assertEqual("Asa", name)

        account1 = account.Account("Asa")
        account1.deposit(2000)

    def test_that_negative_deposit_raises_error(self):
        account1 = account.Account("Stephen")
        account1.deposit(500)
        # account1.deposit(-1000)
        self.assertRaises(ValueError, account1.deposit, -1000)

        self.assertEqual(500, account1.balance)

    def test_money_can_be_withdraw(self):
        account1 = account.Account("Pedro")
        account1.deposit(10000)
        account1.withdraw(5000)
        self.assertEqual(5000, account1.balance)

    def test_that_negative_amount_can_not_be_withdrawn(self):
        account1 = account.Account("Pedro")
        account1.deposit(2000)
        self.assertRaises(ValueError, account1.deposit, -2000)

    def test_that_you_can_withdraw_more_than_your_balance(self):
        account1 = account.Account("Pedro")
        account1.deposit(5000)
        self.assertRaises(ValueError, account1.withdraw, 10000)

    def test_that_money_can_be_transfer(self):
        account1 = account.Account("Asa")
        account2 = account.Account("Pedro")
        account1.deposit(10_000)
        account1.transfer(5_000, account2)
        self.assertEqual(5_000, account1.balance)
        self.assertEqual(5_000, account2.balance)

    def test_that_airtime_can_be_loaded(self):
        account1 = account.Account("Pedro")
        account1.deposit(10000)
        account1.load_airtime(1000)
        self.assertEqual(9000, account1.balance)

    def test_that_money_less_than_50_cant_be_loaded(self):
        account1 = account.Account("Messi")
        account1.deposit(2000)
        self.assertRaises(ValueError, account1.load_airtime, 40)

    # def test_that_account_can_add(self):
    #     result = account.add(2, 5)
    #     self.assertEqual(7, result)
    #
    # def test_subtract(self):
    #     result_minus = account.subtract(10, 5)
    #     self.assertEqual(5, result_minus)


if __name__ == '__main__':
    unittest.main()
