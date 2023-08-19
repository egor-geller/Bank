import re

SPECIAL_CHARS = re.compile('[@_!#$%^&*()<>?/\\|}{~:]')
NUMS = re.compile('[0-9]')


def valid_name(name: str) -> bool:
    if name is None:
        return False
    if len(name) < 2:
        return False
    if SPECIAL_CHARS.search(name) is not None:
        return False
    if NUMS.search(name) is not None:
        return False
    return True


def valid_gender(gender: str) -> bool:
    if gender is None:
        return False
    if gender.lower() != 'male' and gender.lower() != 'female':
        return False
    return True


def valid_age(age: int) -> bool:
    if age is None:
        return False
    try:
        if age < 16:
            return False
        if age > 120:
            return False
    except TypeError:
        return False
    return True


def valid_social_num(social_num: int) -> bool:
    if social_num is None:
        return False
    try:
        if social_num > 999_999_999:
            return False
        if social_num < 10_000:
            return False
    except TypeError:
        return False
    return True
