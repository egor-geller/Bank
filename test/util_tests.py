import unittest
from utils import *


class TestUtils(unittest.TestCase):

    def test_valid_age(self):
        self.assertTrue(valid_age(20), 'age between 16 - 120')
        self.assertFalse(valid_age(121), 'age between 16 - 120')
        self.assertFalse(valid_age('kk'), 'age between 16 - 120')

    def test_valid_social_num(self):
        self.assertTrue(valid_social_num(123123), 'social number between 10_000 - 999_999_999')
        self.assertFalse(valid_social_num(123), 'social number between 10_000 - 999_999_999')

    def test_valid_gender(self):
        self.assertTrue(valid_gender('female'), 'gender is male or female')
        self.assertFalse(valid_gender('fem'), 'gender is male or female')

    def test_valid_name(self):
        self.assertTrue(valid_name('Egor'), 'name must have only alphabetic chars and be greater than 2')
        self.assertFalse(valid_name('Egor123*'), 'name must have only alphabetic chars and be greater than 2')
        self.assertFalse(valid_name('k'), 'name must have only alphabetic chars and be 2 or more chars')


if __name__ == '__main__':
    unittest.main()
