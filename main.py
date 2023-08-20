from log import read_lines
from bank import *


def start_point():
    num = ""
    while num != 0:
        print("1. Open new bank account")
        print("2. How much money left")
        print("3. Deposit a sum of money")
        print("4. Cash withdrawal")
        print("5. Last 10 moves done by the account")
        print("6. Statistics")
        print("To exit press 0")
        num = int(input("Enter a number: "))
        print("\n")
        if num == 1:
            open_bank_account()
            print("\n")
        elif num == 2:
            try:
                acc = int(input("Enter an account number to check the balance: "))
                print(get_current_balance(acc))
                print("\n")
            except ValueError:
                print(f'ValueError: The input is not a number\n')
                continue
        elif num == 3:
            try:
                acc = int(input("Enter an account number: "))
                amount = float(input("Enter amount money to deposit: "))
                deposit(acc, amount)
                print("\n")
            except ValueError:
                print(f'ValueError: The input is not a number\n')
                continue
        elif num == 4:
            try:
                acc = int(input("Enter an account number: "))
                amount = float(input("Enter amount money to withdraw: "))
                withdraw(acc, amount)
                print("\n")
            except ValueError:
                print(f'ValueError: The input is not a number\n')
                continue
        elif num == 5:
            try:
                num_of_lines = int(input("Enter number of lines to read from log: "))
                read_lines(num_of_lines)
                print("\n")
            except ValueError:
                print(f'ValueError: The input is not a number\n')
                continue
        elif num == 6:
            statistics()


if __name__ == '__main__':
    start_point()
