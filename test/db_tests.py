import unittest

from DB import *


class TestUtils(unittest.TestCase):

    def test_is_account_exists(self):
        self.assertFalse(is_account_exists(123))

    def test_has_first_row(self):
        self.assertTrue(has_first_row())


if __name__ == '__main__':
    unittest.main()
