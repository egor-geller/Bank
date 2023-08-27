class AccountDto:

    def __init__(self, account_id: int, name: str, age: int, gender: str, social_num: int, balance: float):
        self.__account_id = account_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__social_num = social_num
        self.__balance = balance

    def get_account_id(self) -> int:
        return int(self.__account_id)

    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return int(self.__age)

    def get_gender(self) -> str:
        return self.__gender

    def get_social_num(self) -> int:
        return int(self.__social_num)

    def get_balance(self) -> float:
        return float(self.__balance)

    def set_balance(self, balance: float) -> None:
        self.__balance = balance

    def __eq__(self, other):
        if isinstance(other, AccountDto):
            return self.__account_id == other.__account_id and self.__name == other.__name and self.__age == other.__age and self.__gender == other.__gender and self.__social_num == other.__social_num and self.__balance == other.__balance
        return False

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(tuple(sorted(self.__dict__.items())))

    def __str__(self):
        return f'Account id: {self.__account_id}\n' \
               f'Name: {self.__name}\n' \
               f'Gender: {self.__gender}\n' \
               f'Social Number: {self.__social_num}\n' \
               f'Balance: {self.__balance}\n'
