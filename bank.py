import names
import random as rd

from log import save_to_log, read_lines
from DB import *
from account import Account
from utils import *


def open_bank_account() -> None:
    num = ""
    while num != 0:
        print("1. Generate X random accounts")
        print("2. Enter manually 1 account")
        print("To go back press 0")
        try:
            num = int(input("Enter a number: "))
            if num == 1:
                generate_accounts()
            if num == 2:
                manual_open_bank_account()
        except ValueError:
            print(f'ValueError: The input is not a number\n')
            continue


def generate_accounts():
    try:
        number_of_accounts = int(input("How many accounts to generate? "))
        for i in range(number_of_accounts):
            if i < number_of_accounts // 2:
                gender = 'male'
            else:
                gender = 'female'
            name = names.get_first_name(gender=gender)
            age = rd.randint(16, 121)
            social_num = rd.randint(100_000, 99_999_999)
            new_account = Account(name, age, gender, social_num)
            save_account(new_account)
            print(new_account)
        print(f"Finish Generating {number_of_accounts} random accounts")
    except ValueError:
        print(f'ValueError: The input is not a number\n')
    except AccountExistsError as e:
        print(e)


def manual_open_bank_account():
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
    except AccountExistsError as e:
        print(e)


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


def transfer_money(acc_from: int, acc_to: int, amount: float) -> None:
    # Take money from account 1
    withdraw(acc_from, amount)

    # Transfer money from account 1 to account 2
    deposit(acc_to, amount)
    save_to_log(f"transfer_money: Account {acc_from} has transferred to account {acc_to} : {amount:.2f}$")


def get_current_balance(account_id: int) -> float:
    acc = read_account(account_id)
    return float(acc.get_balance())


def statistics():
    num = ""
    while num != 0:
        print("1. How much money is in the Bank")
        print("To go back press 0")
        try:
            num = int(input("Enter a number: "))
            if num == 1:
                current_money_in_bank()
        except ValueError:
            print(f'ValueError: The input is not a number\n')
            continue


def current_money_in_bank():
    all_accounts = read_all_accounts()
    money_in_the_bank = sum([float(m.get_balance()) for m in all_accounts])
    print(f"{money_in_the_bank:,.2f}$")


def cash_withdraw():
    try:
        acc = int(input("Enter an account number: "))
        amount = float(input("Enter amount money to withdraw: "))
        withdraw(acc, amount)
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')


def transfer_between_accounts():
    try:
        acc_from = int(input("Enter from which account number transfer: "))
        acc_to = int(input("Enter to which account number transfer to: "))
        amount = float(input("Enter the amount money to transfer: "))
        transfer_money(acc_from, acc_to, amount)
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')


def get_balance():
    try:
        acc = int(input("Enter an account number to check the balance: "))
        print(get_current_balance(acc))
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')


def deposit_amount():
    try:
        acc = int(input("Enter an account number: "))
        amount = float(input("Enter amount money to deposit: "))
        deposit(acc, amount)
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')


def moves_in_bank():
    try:
        num_of_lines = int(input("Enter number of lines to read from log: "))
        read_lines(num_of_lines)
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')


def get_account_details():
    try:
        acc = int(input("Enter an account number: "))
        print(account_details(acc))
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')


def account_details(acc_id: int) -> AccountDto:
    try:
        return read_account(acc_id)
    except AccountNotExistsError as e:
        print(e)


def delete_acc() -> None:
    try:
        acc = int(input("Enter an account number: "))
        delete_account(acc)
        print("\n")
    except ValueError:
        print(f'ValueError: The input is not a number\n')
