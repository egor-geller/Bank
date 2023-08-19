class AccountDto:

    def __init__(self, account_id, name, age, gender, social_num, balance):
        self.__account_id = account_id
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__social_num = social_num
        self.__balance = balance

    def get_account_id(self):
        return self.__account_id

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_social_num(self):
        return self.__social_num

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f'Account id {self.__account_id}\n' \
               f'Name {self.__name}\n' \
               f'Gender {self.__gender}\n' \
               f'Social Number {self.__social_num}\n' \
               f'Balance {self.__balance}\n'
