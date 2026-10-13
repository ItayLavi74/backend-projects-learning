'''
This file is dedicated for functions that
check if the input that provided by the user is valid
'''


def is_valid_amount(amount) -> bool:
    if not amount.isnumeric():
        return False
    return int(amount) > 0


def is_valid_month(month) -> bool:
    if not month.isnumeric():
        return False
    return 1 <= int(month) <= 12


def is_valid_id(id, max) -> bool:
    if not id.isnumeric():
        return False
    return 1 <= int(id) < max


def is_arg_provided(value):
    return value is not None
