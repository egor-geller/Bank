from bank import *


def start_point():
    num = ""
    while num != 0:
        print("1. Open new bank account")
        print("2. Account details")
        print("3. Deposit a sum of money")
        print("4. Cash withdrawal")
        print("5. Transfer money")
        print("6. Last 10 moves in the bank")
        print("7. Statistics")
        print("To exit press 0")
        try:
            num = int(input("Enter a number: "))
        except ValueError:
            print("You have entered an incorrect number")
            print("\n")
            continue
        print("\n")
        if num == 1:
            open_bank_account()
        elif num == 2:
            get_account_details()
        elif num == 3:
            deposit_amount()
        elif num == 4:
            cash_withdraw()
        elif num == 5:
            transfer_between_accounts()
        elif num == 6:
            moves_in_bank()
        elif num == 7:
            statistics()


if __name__ == '__main__':
    start_point()
