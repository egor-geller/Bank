import unittest
import names
import random as rd

from DB import *


class TestUtils(unittest.TestCase):

    existing_account = None
    new_account = None
    read_acc = None
    new_account_id = None

    @classmethod
    def setUpClass(cls) -> None:
        # Generate one existing account
        gender = 'male'
        name = names.get_first_name(gender=gender)
        age = rd.randint(16, 121)
        social_num = rd.randint(100_000, 99_999_999)
        cls.existing_account = Account(name, age, gender, social_num)
        cls.existing_account.set_account_num(72311)

        # Generate one new account
        gender = 'female'
        name = names.get_first_name(gender=gender)
        age = rd.randint(16, 121)
        social_num = rd.randint(100_000, 99_999_999)
        cls.new_account = Account(name, age, gender, social_num)
        cls.new_account_id = cls.new_account.get_account_num()

        # Read one account
        cls.read_acc = read_account(69214)

    @classmethod
    def tearDownClass(cls) -> None:
        delete_account(cls.new_account_id)
        cls.existing_account = None
        cls.new_account = None
        cls.read_acc = None

    def test_save_account(self):
        self.assertRaises(AccountExistsError, save_account, self.existing_account)
        save_account(self.new_account)
        self.assertTrue(is_account_exists(self.new_account.get_account_num()))

    def test_is_account_exists(self):
        self.assertTrue(is_account_exists(self.existing_account.get_account_num()))
        self.assertFalse(is_account_exists(123))

    def test_read_account(self):
        self.assertRaises(AccountNotExistsError, read_account, 123)
        expected_acc = AccountDto(72311, "John", 17, "male", 61187609, 200.0)
        acc_id = self.existing_account.get_account_num()
        actual_acc = read_account(acc_id)
        self.assertEqual(actual_acc, expected_acc, expected_acc)

    def test_has_first_row(self):
        self.assertTrue(has_first_row())

    def test_save_balance(self):
        expected_balance = 300.0
        self.read_acc.set_balance(300)
        save_balance(self.read_acc)
        check_balance = read_account(self.read_acc.get_account_id())
        self.assertEqual(check_balance.get_balance(), expected_balance)


if __name__ == '__main__':
    unittest.main()
