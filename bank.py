from log import save_to_log
from DB import read_account, save_balance, save_account
from account import Account
from utils import *


def open_bank_account() -> None:
    try:
        name = input("Enter person's name (only alphabetic chars): ")
        age = int(input("Enter person's age ( 16 < age < 120 ): "))
        gender = input("Enter person's gender (male or female): ")
        social_num = int(input("Enter peron's social number (6-9 digits): "))
        if not valid_name(name) or not valid_age(age) or not valid_gender(gender) or not valid_social_num(social_num):
            print("Some parameters are incorrect")
            return
        new_account = Account(name, age, gender, social_num)
        save_account(new_account)
        print(new_account)
    except ValueError:
        print(f'ValueError: The input is not a number for age or social number\n')


def deposit(to_account_id: int, amount: float) -> None:
    round_amount = round(amount, 2)
    acc = read_account(to_account_id)
    current_balance = round(float(acc.get_balance()), 2)
    acc.set_balance(current_balance + round_amount)
    save_balance(acc)
    print(f"Account {acc.get_account_id()} balance has been updated, balance is {acc.get_balance()}$")
    save_to_log(f"deposit: Account {acc.get_account_id()} balance has been updated, balance is {acc.get_balance()}$")


def withdraw(from_account_id: int, amount: float) -> None:
    round_amount = round(amount, 2)
    acc = read_account(from_account_id)
    current_balance = round(float(acc.get_balance()), 2)
    if current_balance < round_amount:
        print(f"Insufficient funds, balance available for account {acc.get_account_id()} is {acc.get_balance()}$")
        save_to_log(
            f"Insufficient funds, balance available for account {acc.get_account_id()} is {acc.get_balance()}$")
        return
    acc.set_balance(current_balance - round_amount)
    save_balance(acc)
    print(f"Account {acc.get_account_id()} balance has been updated, balance is {acc.get_balance()}$")
    save_to_log(f"withdraw: Account {acc.get_account_id()} balance has been updated, balance is {acc.get_balance()}$")


def get_current_balance(account_id: int) -> float:
    acc = read_account(account_id)
    return float(acc.get_balance())
