import csv

from Exceptions.AccountExistsError import AccountExistsError
from Exceptions.AccountNotExistsError import AccountNotExistsError
from account import Account
from account_dto import AccountDto

ACCOUNTS_CSV = 'accounts.csv'
COLUMNS = ['AccountID', 'Name', 'Age', 'Gender', 'SocialNum', 'Balance']


def save_account(account: Account) -> None:
    if is_account_exists(account.get_account_num()):
        raise AccountExistsError(f'Account {account.get_account_num()} already exists')

    with open(ACCOUNTS_CSV, 'a') as f:

        # creating a csv writer object
        csvwriter = csv.writer(f)

        # writing the fields
        if not has_first_row():
            csvwriter.writerow(COLUMNS)

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
                return AccountDto(int(lines[0]), lines[1], int(lines[2]), lines[3], int(lines[4]), float(lines[5]))


def save_balance(account):
    if not is_account_exists(account):
        print(f'Account {account} does not exists')
        return
    with open(ACCOUNTS_CSV, 'r') as fr:
        r = csv.reader(fr)
        lines = list(r)

        for line in lines:
            if line[0] == account.get_account_id():
                line[5] = round(account.get_balance(), 2)
                break

    with open(ACCOUNTS_CSV, 'w') as fw:
        writer = csv.writer(fw)
        writer.writerows(lines)


def read_all_accounts() -> []:
    all_accounts = []
    with open(ACCOUNTS_CSV, 'r') as f:
        csv_file = csv.reader(f)

        for lines in csv_file:
            if lines[0] == 'AccountID':
                continue
            acc = AccountDto(int(lines[0]), lines[1], int(lines[2]), lines[3], int(lines[4]), float(lines[5]))
            all_accounts.append(acc)
    return all_accounts


def delete_account(acc_id: int) -> None:
    if not is_account_exists(acc_id):
        print(f'Account with id {acc_id} does not exists')
        return
    print("Acc ID: ", acc_id)
    all_acc = read_all_accounts()
    new_acc = []
    for acc in all_acc:
        if acc.get_account_id() != acc_id:
            print("Acc ID all: ", acc.get_account_id())
            row = [acc.get_account_id(),
                   acc.get_name(),
                   acc.get_age(),
                   acc.get_gender(),
                   acc.get_social_num(),
                   acc.get_balance()]
            new_acc.append(row)

    with open(ACCOUNTS_CSV, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(COLUMNS)
        csvwriter.writerows(new_acc)
