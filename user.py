class User:

    def __init__(self, name, age, gender, social_num):
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__social_num = social_num

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def get_social_num(self):
        return self.__social_num

    def __str__(self):
        return f'Personal details:\n' \
               f'Name: {self.get_name()}\n' \
               f'Age: {self.get_age()}\n' \
               f'Gender: {self.get_gender()}\n' \
               f'Social number: {self.get_social_num()}'
