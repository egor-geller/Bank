import csv

from Exceptions.AccountExistsError import AccountExistsError
from Exceptions.AccountNotExistsError import AccountNotExistsError
from account import Account
from account_dto import AccountDto

ACCOUNTS_CSV = 'accounts.csv'


def save_account(account: Account) -> None:
    columns = ['AccountID', 'Name', 'Age', 'Gender', 'SocialNum', 'Balance']
    if is_account_exists(account.get_account_num()):
        raise AccountExistsError(f'Account {account.get_account_num()} already exists')

    with open(ACCOUNTS_CSV, 'a') as f:

        # creating a csv writer object
        csvwriter = csv.writer(f)

        # writing the fields
        if not has_first_row():
            csvwriter.writerow(columns)

        rows = [[account.get_account_num(),
                 account.get_name(),
                 account.get_age(),
                 account.get_gender(),
                 account.get_social_num(),
                 account.get_balance()]]

        # writing the data rows
        csvwriter.writerows(rows)


def has_first_row() -> bool:
    with open(ACCOUNTS_CSV, 'r') as f:
        csvreader = csv.reader(f)

        for row in csvreader:
            if row[0] == 'AccountID':
                return True
            else:
                return False


def is_account_exists(account_id: int) -> bool:
    with open(ACCOUNTS_CSV, 'r') as f:
        csv_file = csv.reader(f)
        for lines in csv_file:
            if lines[0] == 'AccountID':
                continue
            if int(lines[0]) == account_id:
                return True
        return False


def read_account(account_id: int) -> AccountDto:
    if not is_account_exists(account_id):
        raise AccountNotExistsError(f'Account {account_id} does not exists')

    with open(ACCOUNTS_CSV, 'r') as f:
        csv_file = csv.reader(f)

        for lines in csv_file:
            if lines[0] == 'AccountID':
                continue
            if int(lines[0]) == account_id:
                return AccountDto(lines[0], lines[1], lines[2], lines[3], lines[4], lines[5])


def save_balance(account):
    r = csv.reader(open(ACCOUNTS_CSV, 'r'))
    lines = list(r)

    for line in lines:
        if line[0] == account.get_account_id():
            line[5] = round(account.get_balance(), 2)
            break

    writer = csv.writer(open(ACCOUNTS_CSV, 'w'))
    writer.writerows(lines)
