from user import User
import random as rd
from log import save_to_log


class Account(User):

    def __init__(self, name, age, gender, social_num):
        super().__init__(name, age, gender, social_num)
        self.__balance = 0
        self.__account_num = rd.randint(10_000, 99_999)
        save_to_log(f"New account {self.__account_num} has been created")

    def get_balance(self):
        return self.__balance

    def get_account_num(self):
        return self.__account_num

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def __str__(self):
        return super().__str__() + f"\nBalance is: {self.__balance}$"
